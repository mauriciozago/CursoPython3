cont = 0
lista = list()

while True:
    entrada = int(input('Digite um numero: '))
    lista.append(entrada)
    cont += 1
    while True:
        opcao = str(input('Deseja adicionar mais um numero? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break

lista.sort(reverse=True)

print(f'''
A) Foram digitados {cont} numeros.
B) A lista de valores, ordenada de forma decrescente fica: {lista}''')
print(f'C) O numero 5 está na {lista.index(5)}º posição' if 5 in lista else f'C) O numero 5 não está na lista')
