i = 1

while i != 0:
    sexo = str(input('Entre com o seu sexo [M/F]: ')).upper()

    if sexo == 'M' or sexo == 'F':
        i = 0
    else:
        print('Opção inválida! Tente novamente.')
