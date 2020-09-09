maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Entre com o peso da pessoa {}, em Kg: '.format(c+1)))
    menor = peso * (c == 0) + menor * (c > 0)
    if peso > maior:
        maior = peso
    elif menor > peso:
        menor = peso
print('O maior peso foi {} e o menor peso foi {}!'.format(maior, menor))
