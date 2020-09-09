matrix = [[], [], []]
par = soma = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um numero para Linha {l+1} Coluna {c+1}: '))
        matrix[l].append(n)

for i in matrix:
    for c in i:
        if c % 2 == 0:
            par += c

for j in range(0, 3):
    soma += matrix[j][2]

print(f'''
{matrix[0]}
{matrix[1]}
{matrix[2]}''')

print(f'''
A){par}
B){soma}
C){max(matrix[1])}''')
