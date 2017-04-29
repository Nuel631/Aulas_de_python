#Idade do nadador.

x="s"
while x=="s":


    n=input("digite nome de nadador: ")
    print("Ola"+n )

    i=int(input("digite idade de nadador: "))

    if i>=18:
        print("Adulto")
    elif i>=14:
        print("Juvenil B")
    elif i>=11:
         print("juvenil A")
    elif i>=8:
        print("Infantil B")
    elif i>=5:
        print("Infantil A")
    x=input("quer calcular mais? [s/n]:")
