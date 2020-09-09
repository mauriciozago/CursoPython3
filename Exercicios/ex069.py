cont_mais18 = 0
cont_homens = 0
cont_mulher_menos20 = 0

while True:
    nome = str(input('Entre com o nome: ')).strip()
    idade = int(input('Entre com a idade: '))
    while True:
        sexo = str(input('Entre com o sexo: [M/F] ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
    if sexo == 'M' and idade > 18:
        cont_homens += 1
        cont_mais18 += 1
    elif sexo == 'M' and idade <= 18:
        cont_homens += 1
    elif sexo == 'F' and 18 < idade < 20:
        cont_mais18 += 1
        cont_mulher_menos20 += 1
    elif sexo == 'F' and idade >= 20:
        cont_mais18 += 1
    elif sexo == 'F' and idade <= 18:
        cont_mulher_menos20 += 1
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
        if opcao == 'N':
            break
        elif opcao == 'S':
            print('\n')
            break
    if opcao == 'N':
        break

print(f'''
A) Existem {cont_mais18} pessoas que tem mais de 18 anos!
B) Foram cadastrados {cont_homens} homens!
C) {cont_mulher_menos20} mulher(es) tem menos de 20 anos!
''')
