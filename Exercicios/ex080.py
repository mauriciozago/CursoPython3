lista = list()

for n in range(0, 5):
    while True:
        entrada = int(input('Digite um valor: '))
        if n == 0 or entrada > lista[-1]:
            lista.append(entrada)
            print('Adicionado ao final da lista...')
            break
        elif entrada in lista:
            print('Valor repetido. Digite outro!')
        else:
            pos = 0
            while pos < len(lista):
                if entrada < lista[pos]:
                    lista.insert(pos, entrada)
                    print(f'Adicionado na posição {pos}')
                    break
                pos += 1
            break
print(f'A lista digitada é {lista}!')