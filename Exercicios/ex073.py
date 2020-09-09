tabela = ('Atletico-MG', 'Vasco da Gama', 'Internacional', 'Bahia', 'Athletico-PR', 'Gremio', 'Atletico-GO', 'Santos', 'Fluminense', 'Sport Recife', 'Sao Paulo', 'Flamengo', 'Palmeiras', 'Botafogo', 'Bragantino', 'Corinthians', 'Goias', 'Ceara', 'Fortaleza', 'Coritiba')

print(f'''
A) Os primeiros 5 colocados são {tabela[:5]}
B) Os ultimos 4 colocados são {tabela[-4:]}
C) Os times em ordem alfabética ficam:
{sorted(tabela)}
D) O Coritiba se encontra na {tabela.index('Coritiba')+1} posição
''')
