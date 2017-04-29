#Calculo de IMC.

x="s"
while x=="s":


    sx=input("Digite seu sexo ")
    n=input("Digite seu nome ")
    p=float(input("Digite peso "))
    a=float(input("Digite altura "))
    imc=(p)/(a*a)

    if sx==("Masculino"):

        if imc<20.7:
            print("abaixo do peso")
        elif imc>=20.7:
            print("Peso ideal")
        elif imc>26.4:
            print("Marginalmnete assima do peso")
        elif imc>27.8:
            print("Assima do peso ideal")

    if sx==("Feminino"):

        if imc<19.1:
            print("abaixo do peso")
        elif imc>=19.1:
            print("Peso ideal")
        elif imc>25.8:
            print("Marginalmente assima do peso")
        elif imc>27.3:
            print("Assima do peso ideal")
        x=input("Quer ver de outra pessoa? [s/n]:")
