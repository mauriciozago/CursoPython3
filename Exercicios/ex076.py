produtos = ('OMO', 18,
            'Chocolate', 20,
            'Amaciante', 7,
            'Blusa', 40,
            'Papel Higienico', 15,
            'Feijao', 7,
            'Macarrao', 4.50,
            'Café', 7.50)

print(40*'-')
print(f'{"Loja da Mariusa":^40}')
print(40*'-')

for n in range(0, len(produtos), 2):
    print(f'{produtos[n]:.<30}R${float(produtos[n+1]):>8.2f}')
# {"."*(30 - len(produtos[n]))}
# {" "*(5-len(str(produtos[n+1]))) if type(produtos[n+1]) != float else " "*(7-len(str(produtos[n+1])))}

print(40*'-')
