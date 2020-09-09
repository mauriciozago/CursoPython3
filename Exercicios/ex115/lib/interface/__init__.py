def leiaInt(txt):
    while True:
        try:
            valor = int(input(txt))
            if valor is not None:
                break
        except ValueError:
            print('Valor inválido, por favor entre com um numero inteiro')
    return valor


def linha(tam=42):
    return print('-'*tam)


def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabecalho('PÁGINA PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    linha()
    opcao = leiaInt('Qual a opção desejada? ')
    return opcao
