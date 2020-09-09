from datetime import date

ano = int(date.today().year)
nascimento = int(input('Entre com o seu ano de nascimento: '))

idade = ano - nascimento

if idade < 18:
    print('Faltam {} anos para que voce possa se alistar!'.format(18 - idade))
elif idade == 18:
    print('Está na hora de voce se alistar!')
else:
    print('Voce já passou do tempo do seu alistamento! Regularize-se logo, voce está {} anos atrasado!'.format(
        idade - 18))
