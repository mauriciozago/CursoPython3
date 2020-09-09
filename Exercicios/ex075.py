# n0 = int(input('Digite o primeiro numero: '))
# n1 = int(input('Digite o segundo numero: '))
# n2 = int(input('Digite o terceiro numero: '))
# n3 = int(input('Digite o quarto numero: '))
# tulipa = (n0, n1, n2, n3)

tulipa = (int(input('Digite o primeiro numero: ')), int(input('Digite o segundo numero: ')), int(input('Digite o terceiro numero: ')), int(input('Digite o quarto numero: ')))

print(f'A tupla formada é: {tulipa}')
print(f'Temos {tulipa.count(9)} noves na tupla')
# if tulipa.count(3) == 0:
if 3 in tulipa:
    print(f'Não tem 3 na tupla')
else:
    print(f'O primeiro 3 esta na {tulipa.index(3) + 1} posição')
print(f'Os numeros pares são:', end=' ')
for n in range(0, 4):
    if tulipa[n] % 2 == 0:
        print(tulipa[n], end=' ')
