km = float(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias alugados? '))

print('O valor a pagar pelo aluguel de {} dias e {} Km percorridos é R${:0.2f}'.format(dias, km, (60*dias)+(0.15*km)))
