a=int(input("Escribe un número: "))
b=int(input("Escribe un número mayor que el anterior: "))

for i in range(a, b+1):
    if i%2==0:
        print("El número ",i,"es par")
    else:
        print("El número ",i,"es impar")
