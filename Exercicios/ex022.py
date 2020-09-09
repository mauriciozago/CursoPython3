nome = str(input('Digite seu nome completo: ')).strip()

print('O nome com todas as letras maiusculas fica: {}!'.format(nome.upper()))
print('O nome com todas as letras minusculas fica: {}!'.format(nome.lower()))
print('O nome tem {} letras (sem considerar espaços)!'.format(len(''.join(nome.split()))))
print('O primeiro nome tem {} letras!'.format(len(nome.split()[0])))

