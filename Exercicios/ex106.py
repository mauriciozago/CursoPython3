from time import sleep


def pyhelp():
    while True:
        print('~' * 27)
        print('  SISTEMA DE AJUDA PyHELP  ')
        print('~' * 27)
        a = str(input('Função ou Biblioteca > ')).strip()
        if a.upper() in 'FIM':
            print('~' * 13)
            print('  ATÉ LOGO!  ')
            print('~' * 13)
            break
        print('~' * (36 + len(a)))
        print(f'  Acessando o manual do comando "{a}"  ')
        print('~' * (36 + len(a)))
        sleep(0.5)
        help(a)
        sleep(0.5)


pyhelp()
