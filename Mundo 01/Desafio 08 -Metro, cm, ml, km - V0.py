import emoji
me = float(input('Digite o valor em metros: '))
cm = me * 100
mil = me * 1000
km = me / 1000
cor0 = '\033[m'
cor1 = '\033[4;32;40m'
cor2 = '\033[0;30;43m'
cor3 = '\033[0;30;45m'
ca = emoji.emojize(':motorway:')
print('O valor {}digitado em metros{} foi {}'.format(cor1, cor0, me))
print('{} Metros{} equivale  {} {}centimetros{}'.format(me, ca, cm, cor3, cor0))
print('{} Metros{} {}equivale{} {} milimetros'.format(me, ca, cor2, cor0, mil))
print('{}{} Metros{}{} equivale {} quilometros'.format(cor1, me, ca, cor0, km))

