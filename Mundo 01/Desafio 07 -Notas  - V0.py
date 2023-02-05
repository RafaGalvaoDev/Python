import emoji
nt1 = emoji.emojize(':input_numbers:')
n1 = float(input('Digite sua primeira nota{}: '.format(nt1)))
n2 = float(input('Digite sua segunda nota{}: '.format(nt1)))
me = (n1 + n2) / 2
nt = emoji.emojize(':spiral_notepad:')
cor1 = '\033[4;30;44m'
cor2 = '\033[4;33;40m'
sm = '\033[m'
print('As notas foram {}{} e {}{} '.format(n1, nt, n2, nt))
print('A {}sua media{} foi {}{}{}'.format(cor1, sm, cor2, me, sm))

