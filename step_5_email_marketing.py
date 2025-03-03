
import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    sender_email = "your_email@gmail.com"
    password = "your_email_password"
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, msg.as_string())

email_body = "Hey! The Cloud Couch you were interested in is still available, but only for a limited time. Buy now before the price goes up!"
send_email("customer@example.com", "🔥 Exclusive Offer on Your Dream Couch!", email_body)
print("Retargeting email sent!")
