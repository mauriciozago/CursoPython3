lista = list()
while True:
    while True:
        entrada = int(input('Digite um numero: '))
        if entrada in lista:
            print('Valor já existe na lista, digite outro numero!')
        else:
            lista.append(entrada)
            print('Inserido com sucesso!')
            break

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
lista.sort()
print(lista)
