from random import randint

# n0 = randint(0, 9)
# n1 = randint(0, 9)
# n2 = randint(0, 9)
# n3 = randint(0, 9)
# n4 = randint(0, 9)
#
# lista = (n0, n1, n2, n3, n4)
# arrumado = sorted(lista)
#
# print(f'''
# A lista de numeros é: {lista}
# O menor valor é: {arrumado[0]}
# O maior valor é: {arrumado[4]}
# ''')

lista = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print(f'''
A lista de numeros é {lista}
O menor valor é: {min(lista)}
O maior valor é: {max(lista)}
''')