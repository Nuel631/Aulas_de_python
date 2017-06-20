#Programa calcula o tempo que uma pesso gasta fumando.

c=int(input("Quantos cigarros você fuma por dia ?"))
a=int(input("Há quantos anos você fuma ?"))
a=a*365
minutosTotais = (c*10)*a
total = minutosTotais/1440
print("Dias de vida perdidos %d"%(total))
