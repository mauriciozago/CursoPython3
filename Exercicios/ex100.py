from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for num in range(0, 5):
        lista.append(randint(1, 10))
        sleep(0.5)
        print(lista[num], end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
