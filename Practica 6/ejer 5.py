"""p6e5 - AUTOR: OTTO VASQUEZ
Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista.
Para acabar de escribir los números, escribe un número que no sea mayor que el anterior.
El programa termina escribiendo la lista de números:
Escribe un número: 6
Escribe un número mayor que 6: 10
Escribe un número mayor que 10: 12
Escribe un número mayor que 12: 25
Escribe un número mayor que 25: 9
Los números que has escrito son: 6, 10, 12, 25  (Comentario si os fijáis ya no se imprime
la lista tal cual, hay que imprimir uno por uno los valores de la lista, haced esto así a
partir de ahora)"""

l=[]
a=int(input("Escribe un número: "))
b=int(input(f"Escribe un número mayor que {a}: "))
l.append(a)

while a<=b:
    l.append(b)
    a=b
    b=int(input(f"Escribe una número mayor que {a}: "))
    
print(f"La lista de palabras es:",end=' ')

for i in l:
    print(i,end=' ')

   
