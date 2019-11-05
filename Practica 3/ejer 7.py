d=int(input("Introduce el dia: "))
m=int(input("Introduce el mes: "))
a=int(input("Introduce el año: "))

if (m>12):
    print("Fecha invalida")


elif (m==2):
    if (a%4==0):
        if (d>29):
            print("Fecha invalida")
        else:
            print("Fecha valida")
    else:
        if(d>28):
            print("Fecha invalida")
        else:
            print("Fecha valida")


                    
elif (m==4 or 6 or 9 or 11):
    if (d>30):
            print("Fecha invalida")
    else:
        print("Fecha valida")


elif (m==1 or 3 or 5 or 7 or 8 or 10 or 12):
    if(d>31):
        print("Fecha invalida")
    else:
        print("Fecha valida")

