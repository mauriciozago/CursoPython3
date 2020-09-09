import random

p_aluno = input('Entre com o nome do primeiro aluno: ')
s_aluno = input('Entre com o nome do segundo aluno: ')
t_aluno = input('Entre com o nome do terceiro aluno: ')
q_aluno = input('Entre com o nome do quarto aluno: ')
lista_alunos = [p_aluno, s_aluno, t_aluno, q_aluno]
random.shuffle(lista_alunos)
print('O primeiro aluno é {}! \nO segundo aluno é {}! \nO terceiro aluno é {}! \nO ultimo aluno é {}!'.format(lista_alunos[0], lista_alunos[1], lista_alunos[2], lista_alunos[3]))
