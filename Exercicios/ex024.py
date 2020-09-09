cidade = input('Qual o nome da sua cidade: ').strip()

print('A afirmação que a sua cidade comeca com o nome Santo é {}!'.format('SANTO' in cidade.upper().split()[0]))
