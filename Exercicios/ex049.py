n = int(input('Insira o numero para o qual quer obter a sua tabuada: '))

for c in range(1, 11):
    print('{}x{}={}'.format(n,c,n*c))
