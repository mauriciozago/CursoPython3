while True:
    saque = int(input('Valor a ser sacado: R$ '))
    cinquenta = saque // 50
    vinte = (saque % 50) // 20
    dez = (saque % 50 % 20) // 10
    cinco = (saque % 50 % 20 % 10) // 5
    dois = (saque % 50 % 20 % 10 % 5) // 2
    um = (saque % 50 % 20 % 10 % 5 % 2)

    if cinquenta != 0:
        print(f'Total de {cinquenta} cédula(s) de R$ 50')
    if vinte != 0:
        print(f'Total de {vinte} cédula(s) de R$ 20')
    if dez != 0:
        print(f'Total de {dez} cédula(s) de R$ 10')
    if cinco != 0:
        print(f'Total de {cinco} cédula(s) de R$ 5')
    if dois != 0:
        print(f'Total de {dois} cédula(s) de R$ 2')
    if um != 0:
        print(f'Total de {um} cédula(s) de R$ 1')

    while True:
        opcao = str(input('Deseja fazer outra transação? [S/N] ')).strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
