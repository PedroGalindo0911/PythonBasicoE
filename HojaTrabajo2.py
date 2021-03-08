#Ejercicio 1
x = int(input("Ingresa un número entero positivo: "))
for r in range(x):
    for o in range(r+1):
        print("*", end="" )
    print("")


#Ejercicio 2
n = int(input("Ingresa un número entero positivo: "))
for v in range(n, -1, -1):
    print(v, end=",")




#Ejercicio 3
d = int(input("Introduce un número entero positivo mayor que 2: "))
s = 2
while d % s != 0:
    s+= 1
if s == d:
    print(str(d) + "es primo")
else:
    print(str(d) + "no es primo")
