def leiaInt(txt):
    while True:
        valor = input(txt)
        if valor.isnumeric() == True:
            break
        else:
            print('ERRO! Digite um número inteiro válido')
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
