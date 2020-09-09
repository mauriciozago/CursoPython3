aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'APROVADO!'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO!'
print(f'{aluno["nome"]} está {aluno["situação"]}')
