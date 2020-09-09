from time import sleep


def maior(* num):
    n_maior = 0
    print('-' * 40)
    print('Analisando os valores passados...')
    for a in num:
        sleep(0.5)
        print(a, end=' ')
        if a == num[0]:
            n_maior = a
        elif a > n_maior:
            n_maior = a
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {n_maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
