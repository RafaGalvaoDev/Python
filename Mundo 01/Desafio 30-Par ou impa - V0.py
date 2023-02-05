from emoji import emojize
par = emojize(':keycap_2:')
impa = emojize(':keycap_0:')
cor0 = '\033[m'
cor1 = '\033[0;30;47m'
cor2 = '\033[0;30;42m'
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('{}O número digitado é par {}{}{}'.format(cor1, num, par, cor0))
else:
    print('{}O número digitado é impa {}{}{}'.format(cor2, num, impa, cor0))
