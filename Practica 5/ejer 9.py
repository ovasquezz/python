a=int(input("Escriba la anchura del triangulo: "))
b=int(input("Escriba la altura del triángulo: "))

print("*"*a)
for i in range(b-2):
    print("*"," "*(a-4),"*")
print("*"*a)
