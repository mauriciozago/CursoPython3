n1 = int(input('Nessa série voce vai entrar com 3 numeros! \nO primeiro número é: '))
n2 = int(input('O segundo número é: '))
n3 = int(input('O terceiro número é: '))

if n1 > n2:
    if n1 > n3:
        print('{} é o maior'.format(n1))
    elif n2 > n3:
        print('{} é o menor'.format(n3))
    else:
        print('{} é o maior'.format(n3))
        print('{} é o menor'.format(n2))
else:
    print('{} é o maior'.format(n2))
    print('{} é o menor'.format(n1))