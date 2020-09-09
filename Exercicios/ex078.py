lista = list()

for n in range(0, 5):
    lista.append(int(input(f'Digite o {n+1}º numero: ')))

print(lista)
print(f'O maior valor é {max(lista)} nas posições: ', end='')
for i, n in enumerate(lista):
    if n == max(lista):
        print(f'{i} ', end='')
print()
print(f'O menor valor é {min(lista)} nas posições: ', end='')
for i, n in enumerate(lista):
    if n == min(lista):
        print(f'{i} ', end='')
