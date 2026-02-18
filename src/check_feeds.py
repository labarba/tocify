import json
import os

FEED_HEALTH_PATH = "data/feed_health.json"
REPORT_PATH = "data/bad_feeds_report.md"

def main():
    if not os.path.exists(FEED_HEALTH_PATH):
        print(f"No health file found at {FEED_HEALTH_PATH}")
        return

    with open(FEED_HEALTH_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    bad_feeds = [f for f in data.get("feeds", []) if f["status"] == "error"]

    if not bad_feeds:
        print("All feeds are healthy.")
        # Ensure report file is empty or removed so GHA knows not to open a PR
        if os.path.exists(REPORT_PATH):
            os.remove(REPORT_PATH)
        return

    print(f"Found {len(bad_feeds)} bad feeds. Generating report...")
    
    os.makedirs("data", exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("# 🚨 RSS Feed Maintenance Required\n\n")
        f.write("The following RSS feeds failed during the last digest run:\n\n")
        f.write("| Source | URL | Error |\n")
        f.write("| :--- | :--- | :--- |\n")
        for bf in bad_feeds:
            f.write(f"| {bf['name']} | {bf['url']} | {bf['error']} |\n")
        f.write("\n\nPlease check these feeds in `settings/feeds.txt`.")

    # Set an output for GHA if needed, but checking file existence is often easier
    print(f"Report written to {REPORT_PATH}")

if __name__ == "__main__":
    main()
