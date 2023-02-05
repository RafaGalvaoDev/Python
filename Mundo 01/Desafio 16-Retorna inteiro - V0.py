from math import trunc
from emoji import emojize
inc = emojize(':keycap_1:')
inc1 = emojize(':input_numbers:')
cor0 = '\033[m'
cor1 = '\033[0;30;44m'
cor2 = '\033[0;32;40m'
num = float(input('{}Digite {}um número qualquer:{} '.format(cor1, inc, cor0)))
im = trunc(num)
print('O {}valor inteiro{}{} é {}'.format(cor2, cor0, inc1, im))

