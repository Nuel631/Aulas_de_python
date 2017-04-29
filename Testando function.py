# Teste de function

n1=int(input('Digite primeiro numero: '))
n2=int(input('Digite segundo numero: '))
n3=int(input('Digite terceiro numero: '))
op=int(input("Selecione uma opção = Soma [1] - Maior [2] - Menor [3] - Media [4]"))
s=(n1+n2+n3)
med=s/3


if n1>n2 and n1>n3:
    M=n1
if n2>n1 and n2>n3:
    M=n2
if n3>n1 and n3>n2:
    M=n3



if n1<n2 and n1<n3:
    m=n1
if n2<n1 and n2<n3:
    m=n2
if n3<n1 and n3<n2:
    m=n3

if op==3:
    print('O menor numero é : ',m)
if op==2:
    print('O maior numero é : ',M)
if op==1:
    print('A soma de dos 3 numeros é: ',s)
if op==4:
    print('A media dos numeros é', med)
