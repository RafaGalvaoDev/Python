from math import sqrt
import emoji
numero = int(input('Digite um número: '))
d = numero * 2
t = numero * 3
r = sqrt(numero)
digi = emoji.emojize(':writing_hand:')
mult = emoji.emojize(':keycap_2:')
trip = emoji.emojize(':keycap_3:')
rai = emoji.emojize(':worm:')
cor1 = '\033[0;30;44m'
cor2 = '\033[0;30;41m'
cor3 = '\033[4;30;43m'
sm = '\033[m'
print('O número digitado{} foi {} o seu {}dobro{}{} é {}'.format(digi, numero, cor1, sm, mult, d))
print('O número digitado{} foi {} o seu {}triplo{}{} é {}'.format(digi, numero, cor2, sm, trip, t))
print('O número digitado{} foi {} a sua {}raiz{}{} é {:.2f}'.format(digi, numero, cor3, sm, rai, r))

