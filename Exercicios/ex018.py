import math

angulo = math.radians(float(input('Entre com o valor de um angulo em graus: ')))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O valor do seno do angulo é {:.2f}! \nO valor do cosseno do angulo é {:.2f}! \nE o valor da tangente do angulo é {:.2f}!'.format(seno,cosseno,tangente))