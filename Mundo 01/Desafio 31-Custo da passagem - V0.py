from emoji import emojize
oni = emojize(':bus:')
din = emojize(':money_with_wings:')
cam = emojize(':motorway:')
cor0 = '\033[m'
cor1 = '\033[0;30;44m'
cor2 = '\033[0;30;43m'
passagem = int(input('Digite quantos quilometros pretende viajar: Km '))
valor1 = passagem * 0.50
valor2 = passagem * 0.45
if passagem <= 200:
    print('Sua viagem{}{} é de {}Km'.format(oni,cam, passagem))
    print('{}O valor a ser pago é de{} {:.2f}{}'.format(cor2, cor0, valor1, din))
else:
    print('Sua viagem{}{} é de {}Km'.format(oni, cam, passagem))
    print('{}O valor a ser pago é de{} {:.2f}R${}'.format(cor1, cor0, valor2, din))
