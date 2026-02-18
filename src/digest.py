import os, re, json, time, math, hashlib
from datetime import datetime, timezone, timedelta

import feedparser
import httpx
from dateutil import parser as dtparser
import feedparser
import httpx
from dateutil import parser as dtparser
import llm_wrapper


# ---- load settings ----
def load_llm_settings(path: str = "settings/llm.json") -> dict:
    defaults = {
        "provider": "anthropic",
        "model": "claude-3-haiku-20240307",
        "max_tokens": 8192,
        "batch_size": 25,
        "max_items_per_feed": 50,
        "max_total_items": 600,
        "lookback_days": 7,
        "interests_max_chars": 3000,
        "summary_max_chars": 500,
        "prefilter_keep_top": 300,
        "min_score_read": 0.65,
        "max_returned": 40
    }
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                user_settings = json.load(f)
                defaults.update(user_settings)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {path}, using defaults.")
    return defaults

SETTINGS = load_llm_settings()

# ---- config (env-tweakable, overrides settings/llm.json) ----
def _get_env(key, default, type_cast=str):
    val = os.getenv(key)
    if val is None or val.strip() == "":
        return default
    return type_cast(val)

LLM_PROVIDER = _get_env("LLM_PROVIDER", SETTINGS["provider"]).lower()
MODEL = _get_env("LLM_MODEL", os.getenv("ANTHROPIC_MODEL", SETTINGS["model"]))
MAX_ITEMS_PER_FEED = _get_env("MAX_ITEMS_PER_FEED", SETTINGS["max_items_per_feed"], int)
MAX_TOTAL_ITEMS = _get_env("MAX_TOTAL_ITEMS", SETTINGS["max_total_items"], int)
LOOKBACK_DAYS = _get_env("LOOKBACK_DAYS", SETTINGS["lookback_days"], int)
INTERESTS_MAX_CHARS = _get_env("INTERESTS_MAX_CHARS", SETTINGS["interests_max_chars"], int)
SUMMARY_MAX_CHARS = _get_env("SUMMARY_MAX_CHARS", SETTINGS["summary_max_chars"], int)
PREFILTER_KEEP_TOP = _get_env("PREFILTER_KEEP_TOP", SETTINGS["prefilter_keep_top"], int)
BATCH_SIZE = _get_env("BATCH_SIZE", SETTINGS["batch_size"], int)
MIN_SCORE_READ = _get_env("MIN_SCORE_READ", SETTINGS["min_score_read"], float)
MAX_RETURNED = _get_env("MAX_RETURNED", SETTINGS["max_returned"], int)
MAX_TOKENS = _get_env("MAX_TOKENS", SETTINGS["max_tokens"], int)

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "week_of": {"type": "string"},
        # ranked BEFORE notes so Claude fills articles first and can't exhaust
        # the token budget on a verbose summary before returning any items.
        "ranked": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "id": {"type": "string"},
                    "title": {"type": "string"},
                    "link": {"type": "string"},
                    "source": {"type": "string"},
                    "published_utc": {"type": ["string", "null"]},
                    "score": {"type": "number"},
                    "why": {"type": "string"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["id", "title", "link", "source", "published_utc", "score", "why", "tags"],
            },
        },
        "notes": {"type": "string", "maxLength": 400},
    },
    "required": ["week_of", "ranked", "notes"],
}


# ---- tiny helpers ----
def _strip_md_link(text: str) -> str:
    """Extract bare URL from markdown link syntax [label](url), or return as-is."""
    m = re.match(r'^\[.*?\]\((.*?)\)$', text.strip())
    return m.group(1) if m else text.strip()

def load_feeds(path: str) -> list[dict]:
    """
    Supports:
    - blank lines
    - comments starting with #
    - optional naming via: Name | URL
    - markdown link syntax in the URL column: Name | [url](url)

    Returns list of:
    { "name": "...", "url": "..." }
    """
    feeds = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue

            # Named feed: "Name | URL"
            if "|" in s:
                name, url = [x.strip() for x in s.split("|", 1)]
            else:
                name, url = None, s

            feeds.append({
                "name": name,
                "url": _strip_md_link(url),
            })

    return feeds

def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def load_prompt_template(path: str = "settings/prompt.txt") -> str:
    if not os.path.exists(path):
        # Fallback to current dir for backward compatibility or local dev
        if os.path.exists("prompt.txt"):
            path = "prompt.txt"
        else:
            raise RuntimeError("prompt.txt not found in settings/ or root")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def section(md: str, heading: str) -> str:
    m = re.search(rf"(?im)^\s*#{1,6}\s+{re.escape(heading)}\s*$", md)
    if not m:
        return ""
    rest = md[m.end():]
    m2 = re.search(r"(?im)^\s*#{1,6}\s+\S", rest)
    return (rest[:m2.start()] if m2 else rest).strip()

def parse_interests_md(md: str) -> dict:
    keywords = []
    # Extract all bullet points from the Keywords section (including subsections)
    raw_keywords = section(md, "Keywords")
    for line in raw_keywords.splitlines():
        line_s = line.strip()
        if line_s.startswith("#"):
            continue # ignore subheadings
        line_clean = re.sub(r"^[\-\*\+]\s+", "", line_s)
        if line_clean:
            keywords.append(line_clean)
            
    negative = []
    raw_negative = section(md, "Negative Interests (Exclude)")
    for line in raw_negative.splitlines():
        line_clean = re.sub(r"^[\-\*\+]\s+", "", line.strip())
        if line_clean:
            negative.append(line_clean)

    narrative = section(md, "Narrative").strip()
    if len(narrative) > INTERESTS_MAX_CHARS:
        narrative = narrative[:INTERESTS_MAX_CHARS] + "…"
        
    return {
        "keywords": keywords[:300], # Bumped limit for better coverage
        "negative": negative,
        "narrative": narrative
    }


# ---- rss ----
def parse_date(entry) -> datetime | None:
    for attr in ("published_parsed", "updated_parsed"):
        t = getattr(entry, attr, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    for key in ("published", "updated", "created"):
        val = entry.get(key)
        if val:
            try:
                dt = dtparser.parse(val)
                return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
            except Exception:
                pass
    return None

def fetch_rss_items(feeds: list[dict]) -> tuple[list[dict], list[dict]]:
    """Returns (items, feed_statuses).

    feed_statuses entries:
        name, url, status ("ok" | "empty" | "error"), items_found, error
    """
    cutoff = datetime.now(timezone.utc) - timedelta(days=LOOKBACK_DAYS)
    items = []
    feed_statuses = []

    for feed in feeds:
        url = feed["url"]
        d = feedparser.parse(url)

        # Priority: manual name > RSS title > URL
        source = (
            feed.get("name")
            or d.feed.get("title")
            or url
        ).strip()

        # Determine feed health
        http_status = getattr(d, "status", None)
        error_msg = ""
        if d.bozo and not d.entries:
            feed_status = "error"
            error_msg = str(d.bozo_exception)[:120]
        elif http_status and http_status >= 400:
            feed_status = "error"
            error_msg = f"HTTP {http_status}"
        elif not d.entries:
            feed_status = "empty"
        else:
            feed_status = "ok"

        items_before = len(items)
        for e in d.entries[:MAX_ITEMS_PER_FEED]:
            title = (e.get("title") or "").strip()
            link = (e.get("link") or "").strip()
            if not (title and link):
                continue
            dt = parse_date(e)
            if dt and dt < cutoff:
                continue
            summary = re.sub(r"\s+", " ", (e.get("summary") or e.get("description") or "").strip())
            if len(summary) > SUMMARY_MAX_CHARS:
                summary = summary[:SUMMARY_MAX_CHARS] + "…"
            items.append({
                "id": sha1(f"{source}|{title}|{link}"),
                "source": source,
                "title": title,
                "link": link,
                "published_utc": dt.isoformat() if dt else None,
                "summary": summary,
            })
        items_found = len(items) - items_before

        feed_statuses.append({
            "name": source,
            "url": url,
            "status": feed_status,
            "items_found": items_found,
            "error": error_msg,
        })
        if feed_status != "ok":
            print(f"  [{feed_status.upper()}] {source}: {error_msg or 'no entries'}")

    # dedupe + newest first
    items = list({it["id"]: it for it in items}.values())
    items.sort(key=lambda x: x["published_utc"] or "", reverse=True)
    return items[:MAX_TOTAL_ITEMS], feed_statuses


# ---- local prefilter ----
def keyword_prefilter(items: list[dict], keywords: list[str], keep_top: int) -> list[dict]:
    kws = [k.lower() for k in keywords if k.strip()]
    def hits(it):
        text = (it.get("title","") + " " + it.get("summary","")).lower()
        return sum(1 for k in kws if k in text)
    scored = [(hits(it), it) for it in items]
    matched = [it for s, it in scored if s > 0]
    if len(matched) < min(50, keep_top):
        return items[:keep_top]
    matched.sort(key=hits, reverse=True)
    return matched[:keep_top]


# ---- llm triage ----
def call_llm_triage(interests: dict, items: list[dict]) -> dict:
    lean_items = [{
        "id": it["id"],
        "source": it["source"],
        "title": it["title"],
        "link": it["link"],
        "published_utc": it.get("published_utc"),
        "summary": (it.get("summary") or "")[:SUMMARY_MAX_CHARS],
    } for it in items]

    template = load_prompt_template()

    prompt = (
        template
        .replace("{{KEYWORDS}}", json.dumps(interests["keywords"], ensure_ascii=False))
        .replace("{{NEGATIVE}}", json.dumps(interests.get("negative", []), ensure_ascii=False))
        .replace("{{NARRATIVE}}", interests["narrative"])
        .replace("{{ITEMS}}", json.dumps(lean_items, ensure_ascii=False))
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "generate_digest",
                "description": "Generate a weekly ToC digest from ranked items.",
                "parameters": SCHEMA
            }
        }
    ]

    for attempt in range(6):
        try:
            return llm_wrapper.call_llm_with_tools(
                provider=LLM_PROVIDER,
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                tools=tools,
                tool_choice={"type": "function", "function": {"name": "generate_digest"}},
                max_tokens=MAX_TOKENS
            )
        except Exception as e:
            if attempt == 5:
                raise e
            time.sleep(min(60, 2 ** attempt))

def triage_in_batches(interests: dict, items: list[dict], batch_size: int) -> dict:
    week_of = datetime.now(timezone.utc).date().isoformat()
    total = math.ceil(len(items) / batch_size)
    all_ranked, notes_parts = [], []

    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        print(f"Triage batch {i // batch_size + 1}/{total} ({len(batch)} items)")
        res = call_llm_triage(interests, batch)
        if res.get("notes", "").strip():
            notes_parts.append(res["notes"].strip())
        all_ranked.extend(res.get("ranked", []))

    best = {}
    for r in all_ranked:
        rid = r["id"]
        if rid not in best or r["score"] > best[rid]["score"]:
            best[rid] = r

    ranked = sorted(best.values(), key=lambda x: x["score"], reverse=True)
    
    # Better deduplication: split by sentences and keep unique ones
    all_sentences = []
    for p in notes_parts:
        all_sentences.extend([s.strip() for s in re.split(r'(?<=[.!?])\s+', p) if s.strip()])
    
    unique_notes = []
    seen = set()
    for s in all_sentences:
        if s.lower() not in seen:
            unique_notes.append(s)
            seen.add(s.lower())
            
    return {"week_of": week_of, "notes": " ".join(unique_notes)[:1500], "ranked": ranked}


# ---- render ----
def render_digest_md(result: dict, items_by_id: dict[str, dict]) -> str:
    week_of = result["week_of"]
    notes = result.get("notes", "").strip()
    ranked = result.get("ranked", [])
    
    # Ensure a minimum of 20 articles if possible, otherwise take what's available
    kept = [r for r in ranked if r["score"] >= MIN_SCORE_READ]
    if len(kept) < 20 and len(ranked) >= 20:
        kept = ranked[:20]
    elif len(kept) < 20:
        kept = ranked
    
    kept = kept[:MAX_RETURNED]

    lines = [f"# Weekly ToC Digest (week of {week_of})", ""]
    if notes:
        lines += ["> " + notes.replace("\n", "\n> "), ""]
    lines += [
        f"**Included:** {len(kept)} (score ≥ {MIN_SCORE_READ:.2f})  ",
        f"**Scored:** {len(ranked)} total items",
        "",
        "---",
        "",
    ]
    if not kept:
        return "\n".join(lines + ["_No items met the relevance threshold this week._", ""])

    for r in kept:
        it = items_by_id.get(r["id"], {})
        
        # Defensive extraction with fallbacks from original RSS data (it)
        title = r.get("title") or it.get("title") or "Untitled"
        link = r.get("link") or it.get("link") or "#"
        source = r.get("source") or it.get("source") or "Unknown Source"
        pub = r.get("published_utc") or it.get("published_utc")
        score = r.get("score", 0.0)
        why = r.get("why", "").strip() or "_No reason provided._"
        tags = ", ".join(r.get("tags", [])) if r.get("tags") else ""
        summary = (it.get("summary") or "").strip()

        lines += [
            f"## [{title}]({link})",
            f"*{source}*  ",
            f"Score: **{score:.2f}**" + (f"  \nPublished: {pub}" if pub else ""),
            (f"Tags: {tags}" if tags else ""),
            "",
            why,
            "",
        ]
        if summary:
            lines += ["<details>", "<summary>RSS summary</summary>", '<div class="rss-content">', "", summary, "", "</div>", "</details>", ""]
        lines += ["---", ""]
    return "\n".join(lines)


def main():
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Resolve config paths
    interests_path = "settings/interests.md" if os.path.exists("settings/interests.md") else "interests.md"
    feeds_path = "settings/feeds.txt" if os.path.exists("settings/feeds.txt") else "feeds.txt"
    
    interests = parse_interests_md(read_text(interests_path))
    feeds = load_feeds(feeds_path)
    items, feed_statuses = fetch_rss_items(feeds)

    ok_count = sum(1 for f in feed_statuses if f["status"] == "ok")
    print(f"Fetched {len(items)} RSS items from {ok_count}/{len(feed_statuses)} active feeds (pre-filter)")

    today = datetime.now(timezone.utc).date().isoformat()
    if not items:
        with open("data/digest.md", "w", encoding="utf-8") as f:
            f.write(f"# Weekly ToC Digest (week of {today})\n\n_No RSS items found in the last {LOOKBACK_DAYS} days._\n")
        print("No items; wrote data/digest.md")
        return

    items = keyword_prefilter(items, interests["keywords"], keep_top=PREFILTER_KEEP_TOP)
    print(f"Sending {len(items)} RSS items to model (post-filter)")

    items_by_id = {it["id"]: it for it in items}

    result = triage_in_batches(interests, items, batch_size=BATCH_SIZE)
    result["feed_status"] = feed_statuses
    md = render_digest_md(result, items_by_id)

    with open("data/digest.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("Wrote data/digest.md")

    # Export structured data for the email generator
    with open("data/digest.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print("Wrote data/digest.json")

    # Export feed health as a standalone log
    feed_log = {
        "week_of": result["week_of"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total": len(feed_statuses),
            "ok": sum(1 for f in feed_statuses if f["status"] == "ok"),
            "empty": sum(1 for f in feed_statuses if f["status"] == "empty"),
            "error": sum(1 for f in feed_statuses if f["status"] == "error"),
        },
        "feeds": feed_statuses,
    }
    with open("data/feed_health.json", "w", encoding="utf-8") as f:
        json.dump(feed_log, f, ensure_ascii=False, indent=2)
    print("Wrote data/feed_health.json")


if __name__ == "__main__":
    main()
