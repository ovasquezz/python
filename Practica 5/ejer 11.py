"""P5E11 - AUTOR: OTTO VASQUEZ
Escribe un programa que pida un número e imprima todos sus divisores.
Dame un número: 200
Los divisores de 200 son: 1 2 4 5 8 10 20 25 40 50 100 200"""
L=[]
a=int(input("Dame un numero: "))
for i in range(1,a+1):
    if(a%i==0):
        L=L+[i]
        
print("Los divisores de",a,"son: ",(L))






    

