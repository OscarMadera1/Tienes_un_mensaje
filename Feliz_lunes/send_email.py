from decouple import config
import smtplib, ssl 
from read_csv import df



port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mensajesdnao@gmail.com"  # Enter your address
receiver_email = df['Email']  # Enter receiver address
password = config("EMAIL_PASSWORD")
message = """\
Subject: Hola 

mi primer mensaje en Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print("Correos enviados exitosamente!")