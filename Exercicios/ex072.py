contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')

while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        break

print(f'O numero por extenso corresponde a {contagem[numero]}')
