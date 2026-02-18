# tocify — Weekly Journal ToC Digest

**An AI-powered research assistant that curates a weekly digest of academic journals based on your specific interests.**

This repository runs a GitHub Action once a week (or on-demand) that:
1.  **Fetches** new items from a list of journal RSS feeds (Nature, Science, ArXiv, etc.).
2.  **Triages** items using **any major LLM** (Anthropic, OpenAI, Gemini) to identify papers matching your specific research interests.
3.  **Delivers** a highly polished, responsive HTML email digest directly to your inbox.

---

## 🌟 New Features & Enhancements
Built upon the original vibe-coded proof-of-concept (and this was extended using vibe-coding!), this fork includes significant upgrades:

### 📧 Premium Visual Email Digest
-   **Modern "App-Like" Design**: A completely redesigned HTML template featuring a clean, slate-gray color palette and card-based layout.
-   **Mobile-Optimized**: Responsive CSS ensures the digest looks great on phones and tablets.
-   **Rich Typography**: Integrated **Inter** font family via Google Fonts for excellent readability.
-   **Smart Visuals**:
    -   **Relevance Badges**: Color-coded scores (Green/Amber/Red) to quickly highlight top papers.
    -   **Source Pills**: Clear attribution for each journal source.
-   **Rich Text Support**: Full markdown rendering for AI-generated summaries (bolding, lists, etc.).

### ⚙️ Workflow & Data Improvements
-   **Structured Data Export**: The pipeline now generates a `digest.json` alongside the markdown report, enabling separation of data and presentation.
-   **Repository Hygiene**: The workflow is optimized to **email-only delivery**, keeping your git history clean by not committing weekly reports back to the repo.
-   **Robust Error Handling**: Improved parsing for various RSS date formats and feed structures.

---

## 🚀 Setup & Usage (Fork this Repo)

### 1. Fork & Config
Fork this repository to your own GitHub account.

### 2. Environment Secrets
Go to **Settings → Secrets and variables → Actions** and add the following repository secrets:

**LLM Configuration (Required):**
- `LLM_PROVIDER`: The provider you want to use (e.g., `anthropic`, `openai`, `google`). Can also be set in `settings/llm.json`.
- `LLM_MODEL`: The specific model ID (e.g., `claude-3-haiku-20240307`, `gpt-4o`, `gemini-1.5-pro`). Can also be set in `settings/llm.json`.
- `LLM_API_KEY`: A generic secret for your API key. Alternatively, use provider-specific secrets below.

**Provider-Specific Secrets (Optional):**
- `ANTHROPIC_API_KEY`: For Anthropic Claude models.
- `OPENAI_API_KEY`: For OpenAI GPT models.
- `GOOGLE_API_KEY`: For Google Gemini models.

**Required for Email Delivery:**
-   `SMTP_HOST`: e.g., `smtp.gmail.com`
-   `SMTP_PORT`: e.g., `587`
-   `SMTP_USERNAME`: Your email address.
-   `SMTP_PASSWORD`: Your email password (or [App Password](https://support.google.com/accounts/answer/185833)).
-   `DIGEST_FROM`: The "From" address.
-   `DIGEST_TO`: Where to send the digest.

> [!NOTE]
> Environment variables and GitHub Repository Secrets take precedence over values in `settings/llm.json`.

### 3. Customize Your Interests
Edit `settings/interests.md`. This is the "brain" of the operation.
-   **Keywords**: A list of specific terms to pre-filter articles.
-   **Narrative**: A natural language description of your research focus. The LLM uses this to score relevance.

### 4. Adjust API & Logic Settings
Edit `settings/llm.json`. This folder makes it easy to adjust how the system behaves:
-   **provider**: Match this with your choice in step 2 (anthropic, openai, google).
-   **model**: Specific model ID.
-   **batch_size**: How many articles to process at once.
-   **lookback_days**: How many days back to look for new articles.

### 5. Add/Remove Feeds
Edit `settings/feeds.txt`. Add RSS URLs, one per line. You can optionally name them:
```text
Nature Neuroscience | https://www.nature.com/neuro.rss
https://www.biorxiv.org/rss/subject/neuroscience.xml
```

---

## 🛠 Project Structure

-   **`src/digest.py`**: The core engine. Fetches RSS, filters via keywords, calls the LLM for scoring/summarization, and exports structured data to `data/`.
-   **`src/llm_wrapper.py`**: Abstraction layer for multi-provider support (Anthropic, OpenAI, etc.).
-   **`src/email_digest.py`**: The presentation layer. Reads data from `data/` and generates the sophisticated HTML email.
-   **`settings/`**: Easy-to-adjust configuration folder containing `llm.json`, `feeds.txt`, `interests.md`, and `prompt.txt`.
-   **`data/`**: Stores generated reports and logs (`digest.json`, `digest.md`, etc.).
-   **`.github/workflows/weekly-digest.yml`**: Automation config (runs every Monday).

---

## Credits
Based on the original [*tocify*](https://github.com/voytek/tocify) by [Voytek](https://github.com/voytek). 

**Current Maintainer/Extensions**: [adkarp](https://github.com/adkarp)
