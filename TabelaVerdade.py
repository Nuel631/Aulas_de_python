'''Programa de Raciocínio Lógico e Matemático
   Professor: Agnaldo Cieslak
   Alunos: Erika Klein e Emmanuel Rodrigues
   ADS 1n/ SENAC
   '''

print ("Construa a Tabela Verdade para a fórmula abaixo:")
print ("p v (q ^ r) <-> (p v q) ^ (p v r)")
print ("Digite os valores v ou f para cada proposição:")
print (" ")
print (" ")
print ("Conectivo “e”: (Conjunção)")
print ("Proposições compostas em que está presente o conectivo “e” são ditas CONJUNÇÕES.")
print ("Simbolicamente, esse conectivo pode ser representado por “^”. Então, se temos a sentença:")
print ("Ex: “Emmanuel é estudante e Erika é Bióloga.")
print ("Poderemos representá-la apenas por: p^q. onde: p = Emmanuel é estudante e q = Erika é Bióloga.")
print ("Como se revela o valor lógico de uma proposição conjuntiva? Da seguinte forma:")
print ("Uma conjunção só será verdadeira, se ambas as proposições componentes forem também verdadeiras.")
print (" ")
print (" ")
print ("Conectivo “ou”: (Disjunção)")
print ("Recebe o nome de DISJUNÇÃO toda proposição composta em que as partes estejam unidas pelo conectivo 'ou'.")
print ("Simbolicamente, representaremos esse conectivo por “v”. Portanto, se temos a sentença:")
print ("Ex: “Emmanuel é estudante ou Erika é Bióloga.")
print ("Poderemos representá-la apenas por: pvq. onde: p = Emmanuel é estudante ou q = Erika é Bióloga.")
print ("Uma disjunção será falsa quando as duas partes que a compõem forem ambas falsas! E nos demais casos, a disjunção será verdadeira! .")
print (" ")
print (" ")
print (" Conectivo “ ... se e somente se ...”: (Bicondicional) ")
print ("A estrutura dita bicondicional apresenta o conectivo “se e somente se”, separando as duas sentenças simples.")
print ("Trata-se de uma proposição de fácil entendimento. Se alguém disser: “Emmanuel fica alegre se e somente se Erika sorri.”")
print ("É o mesmo que fazer a conjunção entre as duas proposições condicionais: ")
print ("Emmanuel fica alegre somente se Erika sorri e Erika sorri somente se Emmanuel fica alegre.")
print ("Haverá duas situações em que a bicondicional será verdadeira:")
print ("Quando conseqüentemente forem ambos verdadeiros, ou quando forem ambos falsos")
print ("Nos demais casos, a bicondicional será falsa.")
print (" ")
print (" ")
print ("Tautologia é uma proposição composta formada por duas ou mais proposições p, q, r, ...")
print ("Será dita uma Tautologia se ela for sempre verdadeira, independentemente dos valores lógicos das proposições que a compõem.")
print ("Em palavras mais simples: para saber se uma proposição composta é uma Tautologia, construiremos a sua tabela-verdade!")
print ("Daí, se a última coluna da tabela-verdade só apresentar verdadeiro (e nenhum falso), então estaremos diante de uma Tautologia.")
print (" ")
print ("Tabela verdade")
print (" ")

print ("                                                                                      TAUTOLOGIA          ")
print ("p | q | r | (q ^ r) | (p v q) | (p v r) | p v (q ^ r)| (p v q)^(p v r) | p v (q ^ r) <--> (p v q) ^(p v r)")
print ("__________________________________________________________________________________________________________")
print ("v | v | v |    v    |    v    |    v    |      v     |         v       |              Verdadeiro"          )
print ("__________________________________________________________________________________________________________")
print ("v | v | f |    f    |    v    |    v    |      v     |         v       |              Verdadeiro"          )
print ("________________________________________________________________________________________________________ _")
print ("v | f | v |    f    |    v    |    v    |      v     |         v       |              Verdadeiro"          )
print ("__________________________________________________________________________________________________________")
print ("v | f | f |    f    |    v    |    v    |      v     |         v       |              Verdadeiro"          )
print ("__________________________________________________________________________________________________________")
print ("f | v | v |    v    |    v    |    v    |      v     |         v       |              Verdadeiro"  )
print ("__________________________________________________________________________________________________________")
print ("f | f | v |    f    |    f    |    v    |      f     |         f       |              Verdadeiro")
print ("__________________________________________________________________________________________________________")
print ("f | v | f |    f    |    v    |    f    |      f     |         f       |              Verdadeiro")
print ("__________________________________________________________________________________________________________")
print ("f | f | f |    f    |    f    |    f    |      f     |         v       |              Verdadeiro")
print ("__________________________________________________________________________________________________________")
print (" ")
print (" ")

x="s"
while x=="s":
    def erro(letras):
        i=1
        while i != 0:
            y = input(letras)
            if y != 'v' and y != 'f':
                print("Valor inválido. Digite v ou f")

            else:
                i=0
                return y

    p = erro('Digite um valor para p: ')
    q = erro('Digite um valor para q: ')
    r = erro('Digite um valor para r: ')
    print (" ")
    print (" ")

    if (q=="v") and (r=="v"):
        qer=("v")
    if (q=="v") and (r=="f"):
        qer=("f")
    if (q=="f") and (r=="v"):
        qer=("f")
    if (q=="f") and (r=="f"):
        qer=("f")

    print ("Conjunção (q^r) = "+qer)
    print (" ")
    print (" ")

    if (p=="v") or (q=="v"):
        pouq=("v")
    if (p=="v") or (q=="f"):
        pouq=("v")
    if (p=="f") or (q=="v"):
        pouq=("v")
    if (p=="f") or (q=="f"):
        pouq=("f")

    print ("Disjunção (pvq)= "+pouq)
    print (" ")
    print (" ")

    if (p=="v") or (r=="v"):
        pour=("v")
    if (p=="v") or(r=="f"):
        pour=("v")
    if (p=="f") or (r=="v"):
        pour=("v")
    if (p=="f") or (r=="f"):
        pour=("f")

    print ("Disjunção (pvr)= "+pour)
    print (" ")
    print (" ")


    if (p=="v")or (q=="v") and (r=="v"):
        pouqer=("v")
    if (p=="v")or (q=="v") and (r=="f"):
        pouqer=("v")
    if (p=="v")or (q=="f") and (r=="v"):
        pouqer=("v")
    if (p=="v")or (q=="f") and (r=="f"):
        pouqer=("v")
    if (p=="f")or (q=="v") and (r=="v"):
        pouqer=("v")
    if (p=="f")or (q=="f") and (r=="f"):
        pouqer=("f")
    if (p=="f")or (q=="v") and (r=="f"):
        pouqer=("f")
    if (p=="f")or (q=="f") and (r=="v"):
        pouqer=("f")

    print ("ConjunçãoeDisjunção pv(q^r)= "+pouqer)
    print (" ")
    print (" ")

    if ((p=="v") or (q=="v")) and ((p=='v') or (r=="v")):
        pouqepour=("v")
    if ((p=="v") or (q=="v")) and ((p=='v') or (r=="f")):
        pouqepour=("v")
    if ((p=="v") or (q=="f")) and ((p=='v') or (r=="v")):
        pouqepour=("v")
    if ((p=="v") or (q=="f")) and ((p=='v') or (r=="f")):
        pouqepour=("v")
    if ((p=="f") or (q=="v")) and ((p=='f') or (r=="v")):
        pouqepour=("v")
    if ((p=="f") or (q=="f")) and ((p=='f') or (r=="v")):
        pouqepour=("f")
    if ((p=="f") or (q=="v")) and ((p=='f') or (r=="f")):
        pouqepour=("f")
    if ((p=="f") or (q=="f")) and ((p=='f') or (r=="f")):
        pouqepour=("f")

    print ("DisjunçãoeConjunção (pvq)^(pvr)= "+pouqepour)
    print (" ")
    print (" ")

    if pouqer == pouqepour:
        pouqerpouqepour=("v")

    print ("Bicondição pv(q^r) <--> (pvq)^(pvr)= "+pouqerpouqepour)
    print ("")
    x=input("Quer fazer novamente?")
