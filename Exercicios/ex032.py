ano = int(input('Entre com o ano atual: '))

if ano % 100 == 0:
    if ano % 100 == 0 & ano % 400 == 0:
        print('Esse é um ano bissexto!')
    else:
        print('O ano não é bissexto!')
elif ano % 4 == 0:
    print('Esse é um ano bissexto!')
else:
    print('O ano não é bissexto!')
