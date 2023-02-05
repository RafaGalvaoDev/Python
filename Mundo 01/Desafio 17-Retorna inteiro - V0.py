import math
from emoji import emojize
inc = emojize(':triangular_ruler:')
cor0 = '\033[m'
cor1 = '\033[0;30;43m'
cor2 = '\033[0;30;41m'
cor3 = '\033[0;30;47m'
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
hypo = math.hypot(co, ca)
print('A medida do {}cateto oposto{} foi {}{}'.format(cor1, cor0, co, inc))
print('A medida do {}cateto adjacente{} foi {}{}'.format(cor2, cor0, ca, inc))
print('A {}medida da hipotenusa{} é {:.2f}{}'.format(cor3, cor0, hypo, inc))
