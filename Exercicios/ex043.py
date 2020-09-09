peso = float(input('Entre com o seu peso, em Kg: '))
altura = float(input('Entre com a sua altura, em m: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Voce está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Voce está no peso ideal!')
elif 25 <= imc < 30:
    print('Voce está sobrepeso!')
elif 30 <= imc < 40:
    print('Voce está obeso!')
else:
    print('Voce se encontra em obesidade mórbida!')
