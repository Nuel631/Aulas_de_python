 #o sistema deve perguntar a medida dos 3 lados de um triangulo, o sistema deve informar o tipo de
 #triangulo: equilatero, isosceles ou escaleno.

l1 = int(input('Digite lado um: '))
l2 = int(input('Digite lado dois: '))
l3 = int(input('Digite lado tres: '))

if l1 == l2 & l2 == l3:
    print ('equilatero')
elif l1 == l2 & l2 != l3:
    print ('isosceles')
elif l1 != l2 & l2 == l3:
    print ('isosceles')
elif l3 == l1 & l1 != l2:
    print ('isosceles')
elif l1 != l2 & l2 != l3:
    print ('escaleno')
