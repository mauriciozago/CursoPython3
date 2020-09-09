salario = float(input('Entre com o valor do seu salario: '))

if salario > 1250:
    print('O valor do seu aumento será de R${:.2f}!'.format(salario*1.1-salario))

else:
    print('O valor do seu aumento será de R${:.2f}!'.format(salario*1.15-salario))
