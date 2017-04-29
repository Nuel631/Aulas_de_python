#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#  mostrando uma mensagem de erro e voltando a pedir as informações.

n = (input("Digite seu nome: "))
s = (input("digite uma senha: "))

while n == s:

    print("error")
    n = int(input("Digite seu nome: "))
    s = int(input("digite uma senha: "))
if n != s:
    print("OK")
