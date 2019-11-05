"""P6E1 - AUTOR: OTTO VASQUEZ
Escribe un programa que te pida palabras y las guarde en una lista. Para terminar de introducir palabras, simplemente pulsa Enter. El programa termina escribiendo la lista de palabras.
Escribe una palabra: viaje
Escribe más palabras: aventura
Escribe más palabras: cómic
Escribe más palabras:
Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']"""

l=[]
entrada=input("Escribe una palabra: ")
while entrada!="":
    l.append(entrada)
    entrada=input("Escribe una palabra: ")

print("La lista de palabras es:",l)

