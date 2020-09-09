comp1 = float(input('Nessa série voce terá que entrar com 3 valores de comprimentos \nO primeiro é: '))
comp2 = float(input('O segundo é: '))
comp3 = float(input('O terceiro é: '))

if comp1 > comp2 + comp3 and comp2 > comp1 + comp3 and comp3 > comp1 + comp2:
    print('Não é possível fazer um triangulo com os 3 comprimentos')
elif comp1 == comp2 and comp2 == comp3:
    print('O triangulo formado é EQUILÁTERO!')
elif comp1 == comp2 or comp2 == comp3 or comp1 == comp3:
    print('O triangulo formado é ISÓSCELES!')
else:
    print('O triangulo formado é ESCALENO!')
