from fpdf import FPDF
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from read_csv import df
from decouple import config




 #abrimos archivo txt con formato de contrato
carta_bienvenida = open(r"C:\Users\DARYS\Desktop\DigitalNao\Reto3\Tienes_un_mensaje\contrato.txt", 'r')

def crear_pdf(mensaje_Pdf,carta_bienvenida,nombre_pdf):    
    pdf = FPDF()
    #Agregar pagina
    pdf.add_page()
    pdf.set_font("Arial",'B',16) 
    pdf.cell(400, 10, txt= mensaje_Pdf,align='L')
    pdf.set_font("Arial", size=12) 
    line=1    
    #seleccionar lineas del archivo txt
    for linea in carta_bienvenida:
            #Agregar texto a nuestro archivo pdf    
            pdf.cell(200, 10, txt= linea, ln=line, align='L')
            if linea[-1]==("\n"):
                linea=linea[:-1]
            line+=1       
    
     #Generar archivo pdf
    pdf.output(nombre_pdf)
    pdf.close()


for nombre in df['Name']:
    carta = f"Carta de bienvenida {nombre}.pdf" 
    mensaje_personalizado = f"bienvenido(a) {nombre}"
    crear_pdf(mensaje_personalizado,carta_bienvenida,carta)

 
for correo in df['Email']:
    mensaje = MIMEMultipart('related')
    mensaje['Subject'] = "Carta de bienvenida"
    mensaje['From'] = config('EMAIL')
    mensaje['To'] = correo
    mensaje.attach(MIMEText(mensaje_personalizado))
    
    

    with open(carta, "rb") as f:
        archivo_pdf = MIMEApplication(f.read(), _subtype="pdf")
        archivo_pdf.add_header('content-disposition', 'attachment', filename=carta)
        mensaje.attach(archivo_pdf)

    s= SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(mensaje['From'], config('EMAIL_PASSWORD'))
    s.sendmail(mensaje['From'], [mensaje['To']], mensaje.as_string().encode('utf-8'))
    

    print("Correo "+ mensaje['To'] +" enviado exitosamente!")

s.quit()