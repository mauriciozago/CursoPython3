preco = float(input('Entre com o valor do produto: R$'))
pagamento = int(input('Qual vai ser a forma de pagamento? \nDigite 1 para dinheiro/cheque \nDigite 2 para cartão \nForma de pagamento: '))

if pagamento == 1:
    print('O preço final do seu produto com 10% de desconto fica R${:.2f}!'.format(preco*0.9))
elif pagamento == 2:
    cartao = int(input('Em quantas prestações? '))
    if cartao == 1:
        print('O preço final do seu produto com 5% de desconto fica R${:.2f}!'.format(preco*0.95))
    elif cartao == 2:
        print('O preço final do seu produto será de R${:.2f}, em {} prestações de R${:.2f}!'.format(preco, cartao, preco/cartao))
    else:
        print('O preço final do seu produto com 20% de juros será de R${:.2f}, em {} prestações de R${:.2f}!'.format(preco*1.2, cartao, preco*1.2 / cartao))
else:
    print('Opção de pagamento INVALIDA!')
