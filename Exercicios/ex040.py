n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))

media = (n1 + n2)/2

if n1 > 10 or n2 > 10:
    print('Nota invalida!')
elif media < 5:
    print('A média foi de: {}'.format(media))
    print('REPROVADO!')
elif 5 <= media < 7:
    print('A média foi de: {}'.format(media))
    print('RECUPERAÇÃO!')
else:
    print('A média foi de: {}'.format(media))
    print('APROVADO!')