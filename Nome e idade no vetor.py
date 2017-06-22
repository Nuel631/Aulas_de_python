#Armazena nome e idade no vetor.

i=0
n=[0,0,0,0,0,0,0,0,0,0]
I=[0,0,0,0,0,0,0,0,0,0]

print("Informe 10 nomes e 10 idades, a seguir.")

for i in range(10):
    n[i]=input("Digite nome: ")
    I[i]=input("Digite idade: ")
    i=i+1
print(n)
print(I)
