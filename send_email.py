import os, smtplib
from email.message import EmailMessage

host=os.getenv("SMTP_HOST","smtp.gmail.com")
port=int(os.getenv("SMTP_PORT","587"))
user=os.getenv("SMTP_USER")
password=os.getenv("SMTP_PASSWORD")

if not user or not password:
    raise SystemExit("Set SMTP_USER and SMTP_PASSWORD environment variables.")

to=input("Recipient: ")
subject=input("Subject: ")
body=input("Message: ")

msg=EmailMessage()
msg["From"]=user; msg["To"]=to; msg["Subject"]=subject
msg.set_content(body)

with smtplib.SMTP(host,port) as server:
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
print("Email sent.")
