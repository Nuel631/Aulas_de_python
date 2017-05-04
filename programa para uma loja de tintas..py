#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

L = 80
l = 54
a = float(input('Digite o tamanho em metros quadrados: '))
u = a//l
i = a%l

if a < l:
    print('Você devera comprar 1 lata')
    print('O valor é: R$80,00')

if a > l and i == 0:
    print('Quantidade de latas a serem compradas é de: ',u)
    p = u * L
    print('O valor a ser pago é de: ',p)

elif a> l and i >= 1:
    u = u+1
    print('Quantidades de latas a comprar é de: ',u)
    p = u * L
    print('O valor a ser pago é de: ',p)
