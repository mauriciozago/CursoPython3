n = int(input('Entre com o numero que deseja descobrir se é primo: '))
s = 0

for c in range(1, n):
    if n % c == 0:
        s = s + c
if s == 1:
    print('{} é primo!'.format(n))
else:
    print('{} nao é primo!'.format(n))

