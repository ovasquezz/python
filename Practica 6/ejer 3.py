"""p6e3 AUTOR - OTTO VASQUEZ
Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, escribe una nota que no esté entre 0 y 10. El programa termina escribiendo la lista de notas.
Escribe una nota: 7.5
Escribe una nota: 0
Escribe una nota: 10
Escribe una nota: -1
Las notas que has Escrito son [7.5, 0.0, 10.0]"""

l=[]
entrada=float(input("Escribe una nota: "))
while entrada>=0 and entrada<=10:
    l.append(entrada)
    entrada=float(input("Escribe una nota: "))

print("La lista de notas es:",l)

