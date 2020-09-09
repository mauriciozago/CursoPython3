n1 = int(input('Entre com o primeiro número: '))
n2 = int(input('Entre com o segundo número: '))
opcao = 0
print('''BEM VINDO AO MENU!
ESCOLHA A OPÇÃO QUE MELHOR LHE ATENDE.
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
while opcao != 5:
    opcao = int(input('\nSua opção: '))
    if opcao == 1:
        print('A soma resulta em {}'. format(n1 + n2))
    elif opcao == 2:
        print('A multiplicação resulta em {}'.format(n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        else:
            print('{} é o maior'.format(n2))
    elif opcao == 4:
        n1 = int(input('Qual o seu primeiro novo numero? '))
        n2 = int(input('Qual o seu segundo novo numero? '))
    elif opcao == 5:
        print('Volte Sempre!')
    else:
        print('Opção inválida! Digite uma opção coerente.')
