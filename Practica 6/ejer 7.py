"""p6e7 - AUTOR: OTTO VASQUEZ
Escribe un programa que pida un número (límite) y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14 me cago en todo
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
"""
l=[]
a=int(input("Escribe el límite: "))
b=int(input("Escribe un valor: "))
l.append(b)
suma=0+b

while a>suma:
    b=int(input("Escribe otro valor: "))
    l.append(b)
    suma=suma+b

print("El límite a superar es 50. La lista creada es: ",end='')

for i in l:
    print(i,end=' ')

print(" Ya que la suma de estos números es:",sum(l))
