#programa gera um numero aleatorio entre os numeros digitados.

import random
n1=-1
n2=-1
while (n1 and n2) < 0 :
    n1=float(input("Digite o primeiro numero :"))
    n2=float(input("Digite o segundo numero :"))

aleatorio = random.randint(n1,n2)
print("O numero aleatorio é : %d"%(aleatorio))
