from emoji import emojize
errado = emojize(':cross_mark:')
certo = emojize(':check_mark_button:')
cor0 = '\033[m'
cor1 = '\033[0;30;41m'
cor2 = '\033[0;30;42m'
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano é bissexto{}{}'.format(cor2, cor0, certo))
else:
    print('{}O ano não é bissexto{}{}'.format(cor1, cor0, errado))

