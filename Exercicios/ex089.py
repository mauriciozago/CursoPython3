registro = []
boletim = []
#      0       1     2     3
# [[n_aluno, nt_1, nt_2, media][n_aluno, nt_1, nt_2, media][n_aluno, nt_1, nt_2, media][n_aluno, nt_1, nt_2, media]]
#                0                           1                           2                           3
while True:
    registro.append(str(input('Digite o nome do aluno: ')))
    registro.append(float(input('Digite a primeira nota: ')))
    registro.append(float(input('Digite a segunda nota: ')))
    registro.append(float((registro[1]+registro[2])/2))
    boletim.append(registro[:])
    registro.clear()
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break

print(' No. NOME           MÉDIA ')
print('-'*26)
for n in range(0, len(boletim)):
    print(f' {n}{" "*(4-len(str(n)))}{boletim[n][0]}{float(boletim[n][3]):>12.2f}')
print('-'*26)

while True:
    nr_aluno = int(input('Mostrar notas de qual aluno? '))
    print(f'Notas de {boletim[nr_aluno][0]} são {boletim[nr_aluno][1:3]}')
    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
        if opcao == 'S' or opcao == 'N':
            break
    if opcao == 'N':
        break
