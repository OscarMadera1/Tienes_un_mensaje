import csv

with open('employee_file.csv', mode='w') as csv_file:
    fieldnames = ['Name', 'Email', 'Message']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'Oscar Madera', 'Email': 'omaderanegrete@gmail.com', 'Message': 'Mi primer mensaje'})
    writer.writerow({'Name': 'Ivan Negrete', 'Email': 'mensajesdnao@gmail.com', 'Message': 'Mi primer mensaje'})
