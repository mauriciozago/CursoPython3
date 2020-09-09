while True:
    numero = int(input('Entre com o numero para o qual deseja ver a tabuada: '))
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
print('Volte Sempre!')
