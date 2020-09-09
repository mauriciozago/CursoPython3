from datetime import date

ano = int(date.today().year)
nascimento = int(input('Entre com o seu ano de nascimento: '))

idade = ano - nascimento

if idade <= 9:
    print('Categoria: MIRIM!')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL!')
elif 14 < idade <= 19:
    print('Categoria: JUNIOR!')
elif 19 < idade <= 20:
    print('Categoria: SENIOR!')
else:
    print('Categoria: MASTER!')
