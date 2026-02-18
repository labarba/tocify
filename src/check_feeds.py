import json
import os
import sys

FEED_HEALTH_PATH = "data/feed_health.json"

def main():
    if not os.path.exists(FEED_HEALTH_PATH):
        print(f"No health file found at {FEED_HEALTH_PATH}")
        return

    with open(FEED_HEALTH_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    bad_feeds = [f for f in data.get("feeds", []) if f["status"] == "error"]

    gha_output = os.getenv("GITHUB_OUTPUT")

    if not bad_feeds:
        print("All feeds are healthy.")
        if gha_output:
            with open(gha_output, "a") as f:
                f.write("feeds_failed=false\n")
        return

    print(f"Found {len(bad_feeds)} bad feeds. Generating report...")
    
    report_lines = [
        "# 🚨 RSS Feed Maintenance Required\n\n",
        "The following RSS feeds failed during the last digest run:\n\n",
        "| Source | URL | Error |\n",
        "| :--- | :--- | :--- |\n"
    ]
    for bf in bad_feeds:
        report_lines.append(f"| {bf['name']} | {bf['url']} | {bf['error']} |\n")
    
    report_lines.append("\n\nPlease check these feeds in `settings/feeds.txt`.")
    report_content = "".join(report_lines)

    # Write file for Force-Add strategy
    os.makedirs("data", exist_ok=True)
    with open("data/bad_feeds_report.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    print("Report written to data/bad_feeds_report.md")

    if gha_output:
        # GitHub Action multiline output syntax
        with open(gha_output, "a") as f:
            f.write("feeds_failed=true\n")
            f.write("report_body<<EOF\n")
            f.write(report_content)
            f.write("\nEOF\n")
        print("Report written to GITHUB_OUTPUT")
    else:
        # Local fallback/debug
        print("\n--- REPORT ---")
        print(report_content)
        print("--------------")

if __name__ == "__main__":
    main()
