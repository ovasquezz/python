"""P5E10 - AUTOR: OTTO VASQUEZ
Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
Altura de un triángulo: 5
   *
   ***
  *****
 *******
*********

(a mi me ha quedado mas bonito el triangulo)"""


a=int(input("Escriba la altura del triangulo: "))

for i in range(a+1):
    print(" "*(-i+a),"* "*i)
