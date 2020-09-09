n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n == 999:
        print()
    else:
        soma += n
        cont += 1
print('Foram digitados {} numeros. \nA soma deles é {}!'.format(cont, soma))
