import smtplib
import ssl
from email.message import EmailMessage
from os import getenv

subject = "Email From Python"
body = "Test email from Python"
sender_email = getenv('user_email')
receiver_email = getenv('client_email')
password = getenv('user_password')

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()
# ssl protocole for sending mail from gmail

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print(type(message), type(message.as_string()))
    # message.as_string() - we want to built a string from a message object

print("Succcess")
