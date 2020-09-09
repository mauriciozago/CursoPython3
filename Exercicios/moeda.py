def moeda(valor, tipo='R$'):
    valor = f'{tipo}{valor:0.2f}'.replace('.', ',')
    return valor


def aumentar(valor, pct, fmt=False):
    pct /= 100
    valor *= (1+pct)
    if fmt is True:
        valor = moeda(valor)
    return valor


def diminuir(valor, pct, fmt=False):
    pct /= 100
    valor *= (1-pct)
    if fmt is True:
        valor = moeda(valor)
    return valor


def dobro(valor, fmt=False):
    valor *= 2
    if fmt is True:
        valor = moeda(valor)
    return valor


def metade(valor, fmt=False):
    valor /= 2
    if fmt is True:
        valor = moeda(valor)
    return valor


def resumo(valor, pct_aumento, pct_reducao, currency='R$'):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'''Preço analisado:    {moeda(valor,currency)}
Dobro do preço:     {dobro(valor,True)}
Metade do preço:    {metade(valor, True)}
{pct_aumento}% de aumento:     {aumentar(valor, pct_aumento, True)}
{pct_reducao}% de reducao:     {diminuir(valor, pct_reducao, True)}''')
    print('-'*30)
