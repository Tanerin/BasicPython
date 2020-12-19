#Programa que calcula tu masa corporal
weight = input("Inserta tu peso en kg: ")
height = input("Inserta tu estatura en metros: ")
bmi = round(float(weight)/float(height)**2,2)
print ("Tu indice de masa corporal es: "+str(bmi))