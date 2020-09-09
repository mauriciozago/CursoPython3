p0 = int(input('Entre com o ponto inicial da PA: '))
razao = int(input('Entre com a razão da PA: '))
termos = 11
mais = 1
c = 0

print('Os 10 primeiro termos da PA são: ')
while mais != 0:
    while c < termos:
        print('{}'.format(p0 + (razao * c)), end=' ')
        c += 1
    mais = int(input('\nQuer ver mais quantos termos? '))
    if mais > 0:
        termos = termos + mais
    elif mais == 0:
        c = 0
