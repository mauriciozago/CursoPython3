frase = str(input('Digite uma frase: ')).strip().upper()
se = ''.join(frase.split())
i = 0

for c in range(0, len(se)):
    if se[c] == se[len(se)-1-c]:
        i += 1
if i == len(se):
    print('A frase digitada é um palindromo!')
else:
    print('A frase digitada NÃO é um palindromo!')
