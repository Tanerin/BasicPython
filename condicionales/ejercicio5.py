#Programa para saber si tienes que pagar impuestos
age= int(input("Inserta tu edad: "))
income=int(input("Inserta tus ingresos mensuales: "))
if age > 16 and income >= 1000:
    print("Tienes que pagar impuestos.")
else:
    print("No tienes que pagar impuestos.")