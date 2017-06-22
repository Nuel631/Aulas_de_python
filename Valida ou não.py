#Programa pede uma nota, depois diz se é valida ou não.

n=int(input("Digite uma nota: "));

while n>10 or n<0:
    print ("Nota inválido")
    n=int(input("Digite novamente: "));
if n<10 and n>0:
    print ("Nota válido")
