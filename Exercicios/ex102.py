def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fator = 1
    for valor in range(n, 0, -1):
        fator *= valor

        if show == True:
            if valor == 1:
                print(valor, end=' = ')
            else:
                print(valor, end=' x ')
    return fator


print(fatorial(5, True))
help(fatorial)