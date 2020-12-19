#Progra para saber la nomina por hora trabajada
hours= float(input ("Inserta la cantidad de horas trabajadas: "))
pay = float(input("Inserta el valor del pago: $"))
res= round(pay*hours,3)
print("Tu paga es: $"+str(res))