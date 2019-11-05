a = int(input("Introduzca un número: "))
b = int(input("Introduzca otro número: "))
c = int(input("Introduzca otro número: "))
d = int(input("Introduzca otro número: "))

if d%a==0 and d%b==0 and d&c==0:
    print("El último valor introducido es divisor de los tres primeros.")
else:
    print("El último valor introducido NO es divisor de los tres primeros.")
