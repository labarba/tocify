import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timezone
import markdown

DIGEST_PATH = "digest.md"

def load_digest_md():
    if not os.path.exists(DIGEST_PATH):
        print(f"Error: {DIGEST_PATH} not found.")
        return None
    with open(DIGEST_PATH, "r", encoding="utf-8") as f:
        return f.read()

def md_to_html(md: str) -> str:
    body_html = markdown.markdown(md, extensions=["extra", "nl2br"])
    # Simple, visually appealing wrapper
    return f"""
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8" />
        <style>
          body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f9fafb;
            margin: 0;
            padding: 40px 20px;
            color: #1f2937;
          }}
          .container {{
            max-width: 640px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 8px;
            padding: 32px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
          }}
          h1 {{
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            margin-top: 0;
            margin-bottom: 24px;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 8px;
          }}
          h2 {{
            font-size: 18px;
            font-weight: 600;
            color: #1f2937;
            margin-top: 32px;
            margin-bottom: 12px;
          }}
          p {{
            line-height: 1.6;
            margin-bottom: 16px;
          }}
          a {{
            color: #2563eb;
            text-decoration: none;
          }}
          a:hover {{
            text-decoration: underline;
          }}
          hr {{
            border: none;
            border-top: 1px solid #e5e7eb;
            margin: 32px 0;
          }}
          .meta {{
            color: #6b7280;
            font-size: 12px;
            text-align: center;
            margin-top: 32px;
          }}
          details {{
            background: #f3f4f6;
            padding: 12px;
            border-radius: 4px;
            margin-bottom: 16px;
          }}
          summary {{
            font-weight: 500;
            cursor: pointer;
            color: #4b5563;
          }}
        </style>
      </head>
      <body>
        <div class="container">
          {body_html}
          <div class="meta">
            Sent automatically by your <b>tocify</b> weekly digest workflow.
          </div>
        </div>
      </body>
    </html>
    """

def send_email(html: str, subject: str):
    required_vars = ["SMTP_HOST", "SMTP_USERNAME", "SMTP_PASSWORD", "DIGEST_FROM", "DIGEST_TO"]
    missing = [v for v in required_vars if not os.environ.get(v)]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        return

    sender = os.environ["DIGEST_FROM"]
    recipient = os.environ["DIGEST_TO"]
    host = os.environ["SMTP_HOST"]
    raw_port = os.environ.get("SMTP_PORT")
    port = int(raw_port) if raw_port and raw_port.strip() else 587
    username = os.environ["SMTP_USERNAME"]
    password = os.environ["SMTP_PASSWORD"]

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    # Optional: plaintext fallback using stripped markdown
    plain = "Your weekly ToC digest is available. Please view this email in an HTML-compatible client for the full ranked list."
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))

    print(f"Connecting to {host}:{port}...")
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
    print("Email sent successfully!")

def main():
    md = load_digest_md()
    if not md:
        return
    
    html = md_to_html(md)
    week = datetime.now(timezone.utc).date().isoformat()
    subject = f"Weekly ToC Digest — week of {week}"
    
    send_email(html, subject)

if __name__ == "__main__":
    main()
