import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown2

sender_username = "ENTER_SENDER_USERNAME"
sender_password = "ENTER_SENDER_PASSWORD"
receiver_email = "ENTER_RECEIVER_EMAIL"

def drop_email():
    def read_markdown_file(file_path):
        encodings = ['utf-8', 'utf-8-sig', 'latin-1']
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    markdown_content = file.read()
                return markdown_content
            except UnicodeDecodeError:
                pass
        raise UnicodeDecodeError(f"Unable to decode the file at {file_path} using available encodings")


    sender_email = sender_username
    receiver_email = receiver_email
    subject = 'Chaos on Mongo'
    smtp_server = 'smtp.outlook.com' # ENTER YOUR SMTP URL
    smtp_port = 587 # ENTER YOUR SMTP PORT
    smtp_username = sender_username
    smtp_password = sender_password

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


drop_email()