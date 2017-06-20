#Adivinhe o número.

from random import *

n=randint(0,9)
n2=int(input("Tente adivinhar númeor: "))
i = 0
while n2 != n :
    if n>n2 :
        print("É maior!!")
    elif n<n2:
        print("É menor!!")
    n2= int(input("Tente adivinhar númeor :"))
    i = i + 1
print("Acertouu!!")
print(n)
