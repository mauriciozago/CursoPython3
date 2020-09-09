s = 0
for c in range(1,501):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c
print('A soma dos numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 a 500 é {}!'.format(s))
