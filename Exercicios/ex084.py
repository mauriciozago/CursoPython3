pessoas = list()
dados = list()
peso = list()
maior = list()
menor= list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
print(f'A) Foram cadastradas {len(pessoas)} pessoas!')
for p in pessoas:
    if p[1] == max(peso):
        maior.append(p[0])
    elif p[1] == min(peso):
        menor.append(p[0])
print(f'B) O maior peso foi {max(peso)}. As pessoas cujos pesos são o maior é/são {maior}')
print(f'C) O menor peso foi {min(peso)}. As pessoas cujos pesos são o menor é/são {menor}')
