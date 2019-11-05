a=int(input("Escribe un número: "))
b=int(input("Escribe un número mayor que el anterior: "))
s=0
for i in range(a, b+1):
    s=s+i
print("La suma desde el",a,"hasta el",b,"es:",s)
