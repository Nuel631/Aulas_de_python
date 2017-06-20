#Programa informa se ano é bissexto ou não.

ano=int(input("Digite um ano pra saber se é bissexto: "))
if (ano%4==0) & (ano%100!=0) | (ano%400==0):
    print("O ano é bissexto!")
else:
    print("O ano não é bissexto!")
