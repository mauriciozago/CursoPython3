cont = soma = 0

while True:
    numero = int(input('Entre com um numero: '))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f'Foram digitados {cont} e a soma deles foi de {soma}')
