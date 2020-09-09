from time import sleep
import random

print('Vamos jogar Jokenpo?!')
player = str(input('Sua vez! \nPedra, Papel ou Tesoura! \nQual a sua jogada? ')).upper().strip()
jogadas = ['Pedra', 'Papel', 'Tesoura']
comp = random.choice(jogadas).upper()
print('Eu joguei...')
sleep(3)
print('\n{}'.format(comp))

if player == comp:
    print('\nEMPATOU! Vamos denovo!')
elif player == 'PEDRA' and comp == 'TESOURA':
    print('\nVoce GANHOU! Vamos denovo?')
elif player == 'PEDRA' and comp == 'PAPEL':
    print('\nVoce PERDEU! Vamos denovo?')
elif player == 'PAPEL' and comp == 'TESOURA':
    print('\nVoce PERDEU! Vamos denovo?')
elif player == 'PAPEL' and comp == 'PEDRA':
    print('\nVoce GANHOU! Vamos denovo?')
elif player == 'TESOURA' and comp == 'PAPEL':
    print('\nVoce GANHOU! Vamos denovo?')
elif player == 'TESOURA' and comp == 'PEDRA':
    print('\nVoce PERDEU! Vamos denovo?')
else:
    print('\nVoce jogou errado! PARE DE TRAPACEAR!')
