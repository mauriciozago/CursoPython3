velocidade = int(input('Entre com a velocidade do seu carro, em Km/h: '))

if velocidade > 80:
    print('Voce foi multado em R${}!'.format((velocidade - 80)*7))
else:
    print('Parabéns!')