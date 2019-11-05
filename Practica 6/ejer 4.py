"""p6e4 - AUTOR: OTTO VASSQUEZ
Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero.
El programa termina escribiendo los dos números tal y como se pide:
Escribe un número: 6
Escribe un número mayor que 6: 6
6 no es mayor que 6. Vuelve a introducir un número: 1
1 no es mayor que 6. Vuelve a introducir un número: 8
Los números que has escrito son 6 y 8"""


a=int(input("Escribe un número: "))
b=int(input(f"Escribe un número mayor que {a}: "))

while b<=a:
    b=int(input(f"{b} No es mayor que {a}. Vuelve a introducir un número: "))
    
  
print(f"Los números que has escrito son: {a} y {b}")
