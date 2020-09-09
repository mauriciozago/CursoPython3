frase = input('Digite uma frase: ').strip()

print('A letra a aparece {} vezes na frase!'.format(frase.upper().count('A')))
print('A letra a aparece pela primeira vez na posição {}!'.format(frase.upper().find('A')))
print('A letra a aparece pela ultima vez na posição {}!'.format(frase.upper().rfind('A')))
