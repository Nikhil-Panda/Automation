import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from the Python"
body = "A Test Email"
sender_email = "pandanikhil0408@gmail.com"
receiver_email = "pandanikhil0408@gmail.com"
password = input("Enter the Password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype = "html")
#to set the message type to html 
#if it is a text email then use message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    
print("Success")