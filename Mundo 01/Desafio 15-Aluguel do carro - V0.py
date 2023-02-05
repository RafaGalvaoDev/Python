import emoji
from emoji import emojize
wk = emoji.emojize(':railway_track:')
cr = emoji.emojize(':oncoming_police_car:')
dr = emoji.emojize(':money_with_wings:')
cor0 = '\033[m'
cor1 = '\033[0;30;42m'
cor2 = '\033[0;30;41m'
km = float(input('Quantos {}quilometros{} o carro{} percoreu{}: '.format(cor2, cor0, cr, wk)))
dia = int(input('Por quantos {}dias usou o carro{}{}: '.format(cor1, cor0, cr)))
vd = dia * 60
vkm = (km * 0.15)
soma = vkm + vd
print('O valor a pagar{} por {} dias é de {}R$'.format(dr, dia, vd))
print('O valor a pagar{} por {} km é de {}R$'.format(dr, km, vkm))
print('{}Um total de {}R${}'.format(cor2, soma, cor0))

