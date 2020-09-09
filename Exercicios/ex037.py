numero = int(input('Entre com um numero: '))
print('''Para qual base voce quer converter?
[1] BASE BINÁRIA
[2] BASE OCTAL
[3] BASE HEXADECIMAL''')
opcao = int(input('Qual a sua opção? '))

if opcao == 1:
    print('A conversao do numero {} em binario é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('A conversao do numero {} em octal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('A conversao do numero {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')
