n0 = 0
n1 = 1

n = int(input('Quantos termos voce quer? '))

c = 0
while c < n:
    if c == 0:
        print(0)
        c += 1
    else:
        n2 = n0 + n1
        print(n2)
        n1 = n0
        n0 = n2
        c += 1
