#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve
#informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

v="s"
while v=="s":
    n = int(input('Digite numero: '))
    x = 1
    while x <= 10:
        y = n * x
        print ('%d x %d: %d'%(n,x,y))
        x = x + 1
    v=input("Quer fazer outra dabuada? [s/n]:")
