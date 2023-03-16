from random import choice
print('Olá viajante, Vamos jogar um joguinho? ')
print('Escolha entre papel, pedra e tesoura e veja se pode me vencer ')
escolha = int(input('Digite 1 para Papel\nDigite 2 para Tesoura\nOu digite 3 para Pedra:'))
lista = ['Papel', 'Tesoura', 'Pedra']
ale = choice(lista)

if escolha == 1:
    print('Você escolheu Papel, minha escolha é {}'.format(ale))
elif escolha == 2:
    print('Você escolheu Tesoura, minha escolha é {}'.format(ale))
elif escolha == 3:
    print('Você escolhe Pedra, minha escolha é {}'.format(ale))
    
if ale == lista[0] and escolha == 2 or (ale == lista[1] and escolha == 3) or (ale == lista[2] and escolha == 1):
    print('Você ganhou, Parabéns')
elif ale == lista[0] and escolha == 1 or (ale == lista[1] and escolha == 2) or (ale == lista[2] and escolha == 3):
    print('Empatamos, tente novamente')
elif ale == lista[0] and escolha == 3 or (ale == lista[1] and escolha == 1) or (ale == lista[2] and escolha == 2):
    print('Você perdeu, tente novamente')
else:
    print('Escolha somente entre os números 1 e 3')
