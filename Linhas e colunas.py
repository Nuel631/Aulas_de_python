#Programa cria linas e colunas, de acordo com a quantidade pedida.

l=int(input("Digite a quantidade de linhas: "))
c=int(input("Digite a quantidade de colunas: "))
m = [0]*l
for i in range(l):
    m[i] = [0]*c
print(m)
