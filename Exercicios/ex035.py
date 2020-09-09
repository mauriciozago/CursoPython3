comp1 = float(input('Nessa série voce terá que entrar com 3 valores de comprimentos \nO primeiro é: '))
comp2 = float(input('O segundo é: '))
comp3 = float(input('O terceiro é: '))

if comp1 > comp2 + comp3:
    print('Não é possível fazer um triangulo com os 3 comprimentos')
elif comp2 > comp1 + comp3:
    print('Não é possível fazer um triangulo com os 3 comprimentos')
elif comp3 > comp1 + comp2:
    print('Não é possível fazer um triangulo com os 3 comprimentos')
else:
    print('É possivel fazer um triangulo com os 3 comprimentos')
