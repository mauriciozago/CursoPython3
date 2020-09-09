distancia = float(input('Entre com a distancia da sua viagem, em Km: '))

if distancia > 200:
    print('O valor da sua passagem é R${:.2f}!'.format(distancia*0.45))
else:
    print('O valor da sua passagem é R${:.2f}!'.format(distancia*0.5))
