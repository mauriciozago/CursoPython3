matrix = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um numero para Linha {l+1} Coluna {c+1}: '))
        matrix[l].append(n)

print(f'''
{matrix[0]}
{matrix[1]}
{matrix[2]}
''')
