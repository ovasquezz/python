"""p6e6 - AUTOR: OTTO VASQUEZ
Escribe un programa que pida primero dos números (máximo y mínimo) y
que después te pida números intermedios. Para terminar de escribir números,
escribe un número que no esté comprendido entre los dos valores iniciales.
El programa termina escribiendo la lista de números.
Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
"""

l=[]
a=int(input("Escribe un número: "))
b=int(input(f"Escribe un número mayor que {a}: "))

if b<a:
    b=print(int(input(f"{b} no es mayor que {a}. Vuelve a probar: "))
            
while a<:
    print(int(input("Escribe un número entre {a} y {b}
