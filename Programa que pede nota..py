#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

n = int(input("Digite uma nota entre zero e 10: "))


while n > 10  or n < 0:
    if n > 10 or n < 0:
        print("Comando invalido, digite outro numero.")
    n = int(input("Digite numero: "))
if n < 10 and n > 0:
    print("Valido")
