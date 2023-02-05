from emoji import emojize
vc = emojize(':racing_car:')
vd = emojize(':dollar_banknote:')
vs = emojize(':rescue_worker’s_helmet:')
cor0 = '\033[m'
cor1 = '\033[0;30;41m'
cor2 = '\033[0;30;42m'
cor3 = '\033[4m'
km = float(input('Digite a velocidade do carro{}: Km '.format(vc)))
mut = (km - 80) * 7
print('A sua velocidade foi de {} KM/H'.format(km))
if km > 80:
    print('{}Você foi {}multado por exesso de velocidade{}, o valor a ser pago é de {:.2f} R${}{}{}'.format(cor1, cor3, vc, mut, cor0, vd, vd))
else:
    print('{}Continue digirindo, {}com segurança{}{}{}{}'.format(cor2, cor3, vs, vs,cor0, cor0))
