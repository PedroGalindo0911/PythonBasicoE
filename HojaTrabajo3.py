# Ejercicio 1
x = "contraseña"
contraseña = input("Introduce la contraseña: ")
if x == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")



# Ejercicio 2
nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo (M o H)? ")
if genero == "M":
    if nombre.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if nombre.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)