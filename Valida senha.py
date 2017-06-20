#Sistema valida o cadastro.

senha= "1"
usuario="1"
while senha == usuario:
    usuario=input("Digite o nome de usuario: ")
    senha=input("Digite sua senha: ")
    if senha == usuario:
        print("A senha não pode ser igual a o nome de usuario")
print("Cadastro valido")
