#Leia 10 numeroa e indique o maior.

n = 0
m = 0
x = 0
while (x < 10):
    n = int(input('Entre com um numero: '))
    x = x + 1
    if n > m:
        m = n
print (m)
