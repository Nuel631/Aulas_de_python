#Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
s = 0
m = 0
for i in range(5):
    n = float(input("Digite nota : "))
    s=s+n
    cont=cont+1
    m=(s)/cont
print(s)
print(m)
'''
'''
# 4)
i = 0
while i < 50:
    if (i % 2) == 1:
        print (i)
    i=i+1
