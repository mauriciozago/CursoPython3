def leiaDinheiro(txt):
    cont = 0
    while True:
        entrada = input(txt).replace(',', '.').strip()
        for c in range(0, len(entrada.split('.'))):
            if entrada.split('.')[c].isnumeric():
                cont += 1
        if cont == len(entrada.split('.')):
            break
        else:
            print(f'ERRO: "{entrada}" é um preço inválido!')
    return entrada
