from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da pessoa {}: '.format(c)))
    if date.today().year - nascimento < 21:
        menor += 1
    else:
        maior += 1

print('Segundo os anos de nascimento digitados, temos {} menores e {} maiores.'.format(menor, maior))
