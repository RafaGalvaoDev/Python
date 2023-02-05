from emoji import emojize
cor0 = '\033[m'
cor1 = '\033[0;30;42m'
cor2 = '\033[0;30;41m'
tri = emojize(':triangular_ruler:')
pd = emojize(':check_mark_button:')
np = emojize(':prohibited:')
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r3 + r2 > r1 and r1 + r3 > r2:
    print('{}As retas podem{} formar um triangulo{}{}'.format(cor1, cor0, pd, tri))
else:
    print('{}As retas não podem{} formar um triangulo{}{}'.format(cor2, cor0, np, tri))

