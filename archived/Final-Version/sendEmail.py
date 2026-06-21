import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown2

def drop_email():
    def read_markdown_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        return markdown_content

    sender_email = 'shayan851997@outlook.com'
    receiver_email = 'shayan851997@gmail.com'
    subject = 'Chaos on API'
    smtp_server = 'smtp.outlook.com' 
    smtp_port = 587
    smtp_username = 'shayan851997@outlook.com'
    smtp_password = 'Shayan97@'

    markdown_file_path = './result.md'

    markdown_content = read_markdown_file(markdown_file_path)

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    html_content = markdown2.markdown(markdown_content)

    body = MIMEText(html_content, 'html')
    message.attach(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)

    print("Email sent successfully!")

