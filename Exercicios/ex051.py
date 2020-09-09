p0 = int(input('Entre com o ponto inicial da PA: '))
razao = int(input('Entre com a razão da PA: '))

for c in range(0,11):
    print('O termo {} da PA é {}!'.format(c, p0+(razao*c)))
