expressao = str(input('Digite uma expressão qualquer que use parenteses: ')).strip()
# lista = expressao.split()
# print(lista)
if '(' or ')' in expressao:
    if expressao.count('(') == expressao.count(')'):
        print('OK')
    else:
        print('Sua expressão está errada!')