import random

p_aluno = input('Entre com o nome do primeiro aluno: ')
s_aluno = input('Entre com o nome do segundo aluno: ')
t_aluno = input('Entre com o nome do terceiro aluno: ')
q_aluno = input('Entre com o nome do quarto aluno: ')
print('O aluno escolhido foi o {}!'.format(random.choice([p_aluno,s_aluno,t_aluno,q_aluno])))
