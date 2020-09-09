from random import randint
from time import sleep

jogos = list()
palpite = list()
cont = 0

n = int(input('Quantos jogos deseja fazer? '))

for qnt_jogos in range(0, n):
    while cont < 6:
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
            cont += 1
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    cont = 0

for vizor in range(1, n+1):
    print(f' Jogo {vizor}: {jogos[vizor-1]}')
    sleep(0.5)
