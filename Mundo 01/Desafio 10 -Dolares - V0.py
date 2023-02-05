import emoji
cr = emoji.emojize(':money_bag:')
cd = emoji.emojize(':money_with_wings:')
cor0 = '\033[m'
cor1 = '\033[2;30;42m'
cor2 = '\033[1;30;41m'
din = float(input('Digite quanto em reais você tem na carteira{}: R$ '.format(cr)))
dol = din / 5.50
print('Você pode {}comprar{} com {:.2f}R$ a quantia de {}{:.2f}${}{}'.format(cor1, cor0, din, cor2, dol, cd, cor0))

