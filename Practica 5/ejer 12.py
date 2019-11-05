"""P5E12 - AUTOR: OTTO VASQUEZ
Escribe un programa que pida un número y escriba si primo o no
Dame un número: 123
El número 123 no es primo
Dame un número:127
El número 127 es primo"""

a=int(input("Dame un número: "))
f=0
for i in range(2,a):
    if(a%i==0):
        f=f+1
if(f>0):
    print("El número",a,"no es primo")
else:
    print("El número",a,"es primo")
