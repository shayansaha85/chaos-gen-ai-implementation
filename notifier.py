import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_report(config, html_content):
    sender_email = config.get('email', {}).get('sender_email')
    sender_password = config.get('email', {}).get('sender_password')
    receiver_email = config.get('email', {}).get('receiver_email')
    smtp_server = config.get('email', {}).get('smtp_server')
    smtp_port = config.get('email', {}).get('smtp_port')

    if sender_email == 'YOUR_EMAIL@outlook.com' or not sender_password:
        print("Email not configured in config.yaml. Skipping email notification.")
        return

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Chaos Engineering AI Analysis Report'

    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
