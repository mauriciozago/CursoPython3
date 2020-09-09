nome = str(input('Qual o seu nome? '))
valor = int(input('Qual o valor da casa que deseja comprar? R$'))
salario = int(input('Qual a sua renda mensal? R$'))
prazo = int(input('Em quantos anos pretende pagar a divida? '))

prestacao = valor/prazo

if prestacao > 0.3*salario:
    print('Sr(a) {}, EMPRÉSTIMO NEGADO!'.format(nome))
    print('A prestação da casa ficará maior que 30% do seu salário!')
else:
    print('Sr(a) {}, EMPRÉSTIMO APROVADO!'.format(nome))
    print('A sua prestação será de R${:.2f}!'.format(prestacao))