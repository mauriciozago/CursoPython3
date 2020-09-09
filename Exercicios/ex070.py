print('-'*20)
print('Lojas Mauricio Zago')
print('-'*20)

soma = 0
mais_mil = 0
valor_barato = 0
nome_barato = ''
cont = 0

while True:
    nome_produto = str(input('Insira o nome do produto: ')).lower()
    valor_produto = float(input('Insira o preço do produto: R$ '))
    soma += valor_produto
    cont += 1
    if cont == 1:
        valor_barato = valor_produto
        nome_barato = nome_produto
    elif valor_produto < valor_barato:
        valor_barato = valor_produto
        nome_barato = nome_produto

    if valor_produto > 1000:
        mais_mil += 1

    while True:
        prosseguir = str(input('Deseja continuar comprando? [S/N] ')).upper().strip()
        if prosseguir == 'S' or prosseguir == 'N':
            break
    if prosseguir == 'N':
        break

print(f'''
A) O gasto total da compra foi {soma}!
B) {mais_mil} produtos custaram mais de R$ 1000.00!
C) O produto mais barato foi o(a) {nome_barato}!
''')
