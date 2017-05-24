#contrua um algoritmo que informe a maior e menor idade digitada.


i=0
M=0
m=200
d=int(input('Digite quantas idades serão informadas: '))
for i in range (d):
    n=int(input('Digite valor da idade'))
    if(n>M):
        M=n
    if(n<m):
        m=n


print(M)
print(m)
