pares = list()
impares = list()
numeros = [pares, impares]

for n in range(1, 8):
    entrada = int(input(f'Digite o {n}º numero: '))
    if entrada % 2 == 0:
        pares.append(entrada)
    elif entrada % 2 == 1:
        impares.append(entrada)
pares.sort()
impares.sort()
print(f'Os numeros pares são: {pares}')
print(f'Os numeros impares são: {impares}')
