a=int(input("Quieres calcular el valor de un triángulo (1) o un cuadrado (2): "))

if a==1:
    b=float(input("Introduzca el valor de la base del triángulo: "))
    h=float(input("Introduzca el valor de la altura del triángulo: "))
    print("El area del triángulo es: ", (b*h)/2)
elif a==2:
    l=float(input("Introduzca el valor del lado del cuadrado: "))
    print("El area del cuadrado es: ", l*l)
else:
    print("El número seleccionado no es correcto.")
