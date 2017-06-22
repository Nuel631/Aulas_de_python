#Idade é armazenada no vetor.

a=int(input("Digite quantas vezes você quer informar idade: "))
i=0
n=[]

for i in range(a):
    n.append(int(input("Digite idade: ")))
    i=i+1
print (n)
