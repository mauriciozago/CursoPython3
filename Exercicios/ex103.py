def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))

if jogador == '' and gol == '':
    ficha()
elif jogador == '' and gol.isnumeric():
    gol = int(gol)
    ficha(gols=gol)
else:
    gol = int(gol)
    ficha(jogador, gol)
