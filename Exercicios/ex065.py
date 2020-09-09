n = 0
cont = 0
soma = 0
parar = 0
maior = 0
menor = 0

while parar != 1:
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    erro = 1
    if cont == 1:
        menor = n
    elif n > maior:
        maior = n
    elif menor > n:
        menor = n
    while erro != 0:
        continuar = str(input('Quer continuar?[S/N] ')).upper().strip()
        if continuar == 'S':
            print()
            erro = 0
        elif continuar == 'N':
            parar = 1
            erro = 0
        else:
            print('Opção inválida')
            erro = 1

print('A média dos numeros digitados é {}!'.format(soma/cont))
print('O maior valor é {} e o menor é {}'.format(maior, menor))
