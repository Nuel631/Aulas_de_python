# Media de notas.

x="s"
while x=="s":

    n=input("digite seu nome: ")
    print("Ola "+n)
    n1=float(input("digite N1: "))
    n2=float(input("digite N2: "))
    n3=float(input("digite N3: "))
    n4=float(input("digite N4: "))
    m=(n1+n2+n3+n4)/4
    print("Ola %s, vou exibir sua nota:"%n)
    print(m)
    print("Ola %s, sua nota foi: %4.2f"%(n,m))
    if m>=9:
        print("Ótimo")
    elif m>=7:
        print("Bom")
    elif m>=6:
        print("suficiente")
    else:
        print("insufisiente")
    x=input("quer calcular mais??")
