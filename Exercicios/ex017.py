import math

co = int(input('Entre com o comprimento do cateto oposto: '))
ca = int(input('Entre com o comprimento do cateto adjacente: '))

print('O valor da hipotenusa que tem como cateto oposto {} e cateto adjacente {} é {}!'.format(co,ca,math.hypot(co, ca)))

