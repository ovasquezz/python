a = int(input("Introduzca un número: "))
b = int(input("Introduzca otro número: "))
c = int(input("Introduzca otro número: "))
d = int(input("Introduzca otro número: "))
e = int(input("Introduzca otro número: "))

if a<b<c<d<e:
    print("Los números eestan en orden ascendente")
elif a>b>c>d>e:
    print("Los números estan en orden descendente")
else:
    print("Los valores estan desordenados")
