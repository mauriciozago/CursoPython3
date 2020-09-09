palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for n in palavras:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    # if n.count('a') != 0:
    #     print(n.count('a')*'a ', end='')
    # if n.count('e') != 0:
    #     print(n.count('e')*'e ', end='')
    # if n.count('i') != 0:
    #     print(n.count('i')*'i ', end='')
    # if n.count('o') != 0:
    #     print(n.count('o')*'o ', end='')
    # if n.count('u') != 0:
    #     print(n.count('u')*'u ', end='')
