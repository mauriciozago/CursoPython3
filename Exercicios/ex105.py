def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = dict()
    dicionario["Quantidade de notas"] = len(valores)
    dicionario["Maior nota"] = max(valores)
    dicionario["Menor nota"] = min(valores)
    dicionario["Média da turma"] = sum(valores)/len(valores)
    if sit == True:
        if dicionario["Média da turma"] >= 7.0:
            dicionario["A situação"] = 'BOA'
        elif 5.0 <= dicionario["Média da turma"] < 7.0:
            dicionario["A situação"] = 'RAZOÁVEL'
        else:
            dicionario["A situação"] = 'RUIM'
    return dicionario


relatorio = notas(5.5, 9.5, 10, 6.5, sit=True)
print(relatorio)
help(notas)