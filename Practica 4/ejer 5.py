I=int(input("Introduzca el importe que desee extraer: "))
E=0
if I%500==0:
    print("el cajero te devuelve",E,"billetes de 500€")
elif(I%200==0):
    E=I/200
    print("el cajero te devuelve",E,"billetes de 200€")
elif(I%100==0):
    E=I/100
    print("el cajero te devuelve",E,"billetes de 100€")
elif(I%50==0):
    E=I/50
    print("el cajero te devuelve",E,"billetes de 50€")
elif(I%20==0):
    E=I/20
    print("el cajero te devuelve",E,"billetes de 20€")
elif(I%10==0):
    E=I/10
    print("el cajero te devuelve",E,"billetes de 10€")
elif(I%5==0):
    E=I/5
    print("el cajero te devuelve",E,"billetes de 5€")
else:
    print("lo siento,no le puedo dar el importe deseado")
    
