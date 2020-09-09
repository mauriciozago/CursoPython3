from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    elif passo < 0:
        passo *= -1
    print('-' * 40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio <= fim:
        b = 1
    elif inicio > fim and passo < 0:
        b = -1
    elif inicio > fim and passo > 0:
        b = -1
        passo *= -1
    for a in range(inicio, fim + b, passo):
        sleep(0.25)
        print(a, end=' ')
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
