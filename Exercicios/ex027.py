nome = input('Digite seu nome completo: ').strip()

print('Seu primeiro nome é: {}! \nSeu ultimo nome é: {}!'.format(nome.split()[0], nome.split()[len(nome.split())-1]))
