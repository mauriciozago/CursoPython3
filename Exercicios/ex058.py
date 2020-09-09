from random import randint

numero = int(randint(0, 10))
chute = 11
i = 0

while chute != numero:
    chute = int(input('Chute o valor do random (De 0 a 10): '))
    i += 1
    if chute != numero:
        print('ERROU! Tente denovo!')
    else:
        print('ACERTOU!')
print('Voce precisou de {} palpites para acertar!'.format(i))
