import email.message
from decouple import config
import smtplib
from convert_to_time import df 
from plantilla import plantillaMsg
import datetime 
import pandas as pd






class Email:
    
    def __init__(self,sender_email,password):
        self.sender_email = sender_email
        self.password = password
               
                    
    def enviarMsg(self,receiver_email,message):  
        self.receiver_email = receiver_email # Enter receiver address        
        self.message = message # Enter you message 

        server = smtplib.SMTP('smtp.gmail.com:587')
        
        email_content = self.message

        msg = email.message.Message()

        dia = datetime.datetime.now()

     

        
        for mes in df['month']:
            print()
            for day in df['day']:
                print()

        if mes== dia.month and day == dia.day:

            msg['Subject'] = 'Feliz cumpleaños'
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            password = self.password
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            
            s= smtplib.SMTP('smtp.gmail.com:587')
            s.starttls()
            # Login Credentials for sending the mail 
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())


            print("Correo "+ msg['To'] +" enviado exitosamente!")
        


Gmail = Email(config("EMAIL"),config("EMAIL_PASSWORD"))

Gmail.enviarMsg(df['Email'],plantillaMsg)