"""p6e2 - AUTOR: OTTO VASQUEZ
Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. El programa termina escribiendo la lista de números.
Escribe un nombre: 14
Escribe una otro nombre: 123
Escribe una otro nombre: -25
Escribe una otro nombre: 123
Escribe una otro nombre: Salir
Los números que has escrito son [14, 123, -25, 123]"""

l=[]
entrada=input("Escribe un número: ")
while entrada!="salir":
    l.append(entrada)
    entrada=input("Escribe un número: ")

print("La lista de nñumero es:",l)

