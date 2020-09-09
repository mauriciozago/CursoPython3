numero = int(input('Entre com o numero que deseja saber o valor do fatorial: '))
fatorial = 1
c = numero
# for c in range(numero, 0, -1):
#     fatorial = fatorial * c
#
# print('O valor do fatorial é {}!'.format(fatorial))

while c != 0:
    fatorial = fatorial * c
    c -= 1

print('O valor do fatorial é {}!'.format(fatorial))
