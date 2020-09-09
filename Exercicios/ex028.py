import random

numero = int(random.randint(0,5))
chute = int(input('Chute o valor do random (De 0 a 5): '))
n = str(numero)

print('O valor do random foi: {}'.format(n))
print('Voce acertou!' if numero == chute else 'Voce errou!')
