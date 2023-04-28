import datetime
import csv


"""
df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'],format="%Y/%m/%d")

df['year'] = df['FechaNacimiento'].dt.year
df['month'] = df['FechaNacimiento'].dt.month
df['day'] = df['FechaNacimiento'].dt.day"""

today = datetime.datetime.now()
nombres =[]
direcciones_correo = []
with open(r'C:\Users\DARYS\Desktop\DigitalNao\Reto3\Tienes_un_mensaje\employee.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    encabezados = next(lector_csv) 

    for fila in lector_csv:
        nombre = fila
        fecha_Nacimiento = datetime.datetime.strptime(fecha_Nacimiento, '%Y-%m-%d').date()

        if fecha_Nacimiento.month == today.month and fecha_Nacimiento.day == today.day:
            nombres.append(nombre)
            direcciones_correo.append(correo)

print(nombres)
print(direcciones_correo)