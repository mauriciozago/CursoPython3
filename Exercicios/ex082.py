lista = list()
par = list()
impar = list()

while True:
    entrada = int(input('Digite um numero: '))
    lista.append(entrada)
    while True:
        opcao = str(input('Desejar inserir mais um numero? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

lista.sort()
par.sort()
impar.sort()

print(f'''
{lista}
{par}
{impar}
''')
