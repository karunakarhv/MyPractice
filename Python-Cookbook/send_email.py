# Send the response to email
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

def send_email(subject, body, to_email):
    load_dotenv()
    from_email=os.getenv('FROM_EMAIL')
    smtp_server=os.getenv('SMTP_SERVER')
    smtp_port=int(os.getenv('SMTP_PORT'))
    smtp_username=os.getenv('SMTP_USERNAME')
    smtp_password=os.getenv('SMTP_PASSWORD')
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    print(f"Sending email to {to_email} with subject: {subject}")
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
    print(f"Email sent to {to_email}")
