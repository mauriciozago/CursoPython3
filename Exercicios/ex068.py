from random import randint

cont = 0

while True:
    n_cpu = randint(0, 10)
    # cpu = randint(1, 2)
    # lista = ['PAR', 'IMPAR']
    n_jogador = int(input('Diga um valor de 0 a 10: '))
    jogador = str(input('Par ou Impar? [P/I] ')).strip().upper()
    soma = n_cpu + n_jogador

    print(f'\nEu joguei {n_cpu}!')

    if soma % 2 == 0 and jogador == 'P':
        print('''\nVoce ganhou!
VAMOS DENOVO...
''')
        cont += 1
    elif soma % 2 == 0 and jogador == 'I':
        print('\nVoce perdeu!')
        break
    elif soma % 2 == 1 and jogador == 'P':
        print('\nVoce perdeu!')
        break
    elif soma % 2 == 1 and jogador == 'I':
        print('''\nVoce ganhou!
VAMOS DENOVO...
''')
        cont += 1
    else:
        print('ERRO!')

print(f'\nVoce ganhou {cont} partida(s) consecutiva(s)!')
