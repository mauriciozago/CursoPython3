def escreva(txt):
    print('-'*(len(txt)+2))
    print(f' {txt} ')
    print('-'*(len(txt)+2))


mensagem = str(input('Digite a mensagem que deseja exibir: '))
escreva(mensagem)
