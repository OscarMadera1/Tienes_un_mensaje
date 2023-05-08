from decouple import config
import smtplib, ssl 
from read_csv import df
from datetime import datetime

lunes = datetime.now().weekday() # Obtener dia de la semana

if lunes == 0: # Comparar dia de la semana
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "mensajesdnao@gmail.com"  # Introducir correo de origen
    receiver_email = df['Email']  # Introducir correo que recibe
    password = config("EMAIL_PASSWORD") # Contraseña de correo 
    message = """\   
    Subject: Feliz lunes

    Buenos dias, 
    Es momento de iniciar una nueva semana y te queremos desear exito!."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("Correos enviados exitosamente!")
else:
    print("Hoy, no es lunes!")