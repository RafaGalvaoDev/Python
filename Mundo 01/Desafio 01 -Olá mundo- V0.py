import emoji
azul = '\033[4;36;40m'
vazio = '\033[m'
verde = '\033[0;30;42m'
invader = emoji.emojize(':alien_monster:')
mundo = emoji.emojize(':globe_showing_Americas:')
vermelho = '\033[4;30;41m'
print('{}Olá{} {}Planeta{} terra {}'.format(azul, vazio, verde, vazio, mundo))
print('Você esta sendo {}invadido{}'.format(vermelho, vazio))
print('{}{}{}{}{}'.format(invader, invader, invader, invader, mundo))
print('{}{}{}{}{}'.format(invader, invader, invader, mundo, invader))
print('{}{}{}{}{}{}{}'.format(vermelho, invader, invader, mundo, invader, invader, vazio))

