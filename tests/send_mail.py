import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Jenkins details
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "Python_Selenium"
USERNAME = "admin"
API_TOKEN = "1172001a83e9654b0e67f1e57814368f82"

# Email details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "akhilagangadharuppin@gmail.com"
APP_PASSWORD = "zafm trio afeq uxah"  # Never hardcode this in production
RECEIVER_EMAIL = "akhilagangadharuppin@gmail.com"


def fetch_jenkins_job_details():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    try:
        response = requests.get(url, auth=(USERNAME, API_TOKEN), timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch Jenkins job details: {e}")


def build_email_content(build_info):
    build_number = build_info.get("number")
    status = build_info.get("result")
    duration = build_info.get("duration", 0) // 1000  # milliseconds to seconds
    url = build_info.get("url")

    color = "green" if status == "SUCCESS" else "red"

    content = f"""
    <html>
    <body>
        <h2>Jenkins Build Report</h2>
        <ul>
            <li><strong>Job:</strong> {JOB_NAME}</li>
            <li><strong>Build Number:</strong> {build_number}</li>
            <li><strong>Status:</strong> <span style="color:{color};">{status}</span></li>
            <li><strong>Duration:</strong> {duration} seconds</li>
            <li><strong>URL:</strong> <a href="{url}">{url}</a></li>
        </ul>
    </body>
    </html>
    """
    return content


def send_email(subject, html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    part = MIMEText(html_content, "html", "utf-8")
    msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("✅ Email sent successfully.")
    except smtplib.SMTPException as e:
        raise Exception(f"SMTP error: {e}")


def main():
    try:
        build_info = fetch_jenkins_job_details()
        html_content = build_email_content(build_info)
        subject = f"Jenkins Job Report: {JOB_NAME} - Build #{build_info['number']} [{build_info['result']}]"
        send_email(subject, html_content)
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
