soma = 0
cont = 0
velho = 0
nome_velho = ''
for c in range(1, 5):
    nome = str(input('Entre com o nome da pessoa {}: '.format(c))).strip()
    idade = int(input('Entre com a idade da pessoa {}: '.format(c)))
    sexo = str(input('Entre com o sexo da pessoa {} (M ou F): '.format(c))).upper().strip()
    soma = soma + idade

    if idade > velho and sexo == 'M':
        nome_velho = nome
        velho = idade

    if idade < 20 and sexo == 'F':
        cont += 1

print('A media de idade do grupo é {}!'.format(soma/c))
print('O nome do homem mais velho é {}!'.format(nome_velho))
print('{} mulheres tem menos de 20 anos!'.format(cont))
