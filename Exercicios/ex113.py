# def leiaInt(txt):
#     while True:
#         valor = str(input(txt)).strip()
#         if valor.isnumeric() is True:
#             break
#         else:
#             print('ERRO! Digite um número inteiro válido')
#     return valor
#
# def leiaFloat(txt):
#     cont = 0
#     while True:
#         valor = str(input(txt)).strip()
#         for n in range(0, len(valor.split('.'))):
#             if (valor.split('.'))[n].isnumeric() is True:
#                 cont += 1
#         if cont == len(valor.split('.')):
#             break
#         else:
#             print('ERRO! Digite um número inteiro válido')
#     return valor

def leiaInt(txt):
    while True:
        try:
            valor = int(input(txt))
            if valor is not None:
                break
        except ValueError:
            print('Erro de Entrada')
        except KeyboardInterrupt:
            print('Não quis digitar')
            valor = 0
            break
    return valor


def leiaFloat(txt):
    while True:
        try:
            valor = float(input(txt))
            if valor is not None:
                break
        except ValueError:
            print('Erro de Entrada')
        except KeyboardInterrupt:
            print('Não quis digitar')
            valor = 0
            break
    return valor


entrada = leiaInt('Digite um inteiro: ')
entrada2 = leiaFloat('Digite um float: ')
print(f'Você acabou de digitar o número {entrada} e {entrada2}')
