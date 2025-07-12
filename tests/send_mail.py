import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Jenkins details
JENKINS_URL = "http://localhost:8080/"
JOB_NAME = "your-job-name"
USERNAME = "your-jenkins-username"
API_TOKEN = "your-api-token"

# Email details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_gmail_app_password"
RECEIVER_EMAIL = "receiver_email@example.com"


def fetch_jenkins_job_details():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    response = requests.get(url, auth=(USERNAME, API_TOKEN))

    if response.status_code != 200:
        raise Exception(f"Failed to fetch Jenkins job details. Status: {response.status_code}")

    return response.json()


def build_email_content(build_info):
    build_number = build_info.get("number")
    status = build_info.get("result")
    duration = build_info.get("duration") // 1000
    url = build_info.get("url")

    content = f"""
    <h2>Jenkins Build Report</h2>
    <ul>
        <li><strong>Job:</strong> {JOB_NAME}</li>
        <li><strong>Build Number:</strong> {build_number}</li>
        <li><strong>Status:</strong> <span style="color:{'green' if status == 'SUCCESS' else 'red'};">{status}</span></li>
        <li><strong>Duration:</strong> {duration} seconds</li>
        <li><strong>URL:</strong> <a href="{url}">{url}</a></li>
    </ul>
    """
    return content


def send_email(subject, html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    part = MIMEText(html_content, "html")
    msg.attach(part)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("✅ Email sent successfully.")


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
