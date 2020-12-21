#Grupo que divide gente segun unos parametros
name = input("Como tu te llama: ")
gender = input("Cual es tu sexo (M/H): ")
if gender =="M":
    
    if name.lower() < "m":
        group="A"
    else:
        group="B"
else:
    if name.lower() > "n":
        group="A"
    else:
        group="B"
print("Tu grupo es: "+group)
