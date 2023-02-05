import math
from emoji import emojize
tri = emojize(':triangular_ruler:')
cor0 = '\033[m'
cor1 = '\033[0;30;47m'
cor2 = '\033[0;30;42m'
ang = float(input('Digite o valor de um angulo qualquer: '))
ra = math.radians(ang)
sen = math.sin(ra)
con = math.cos(ra)
tan = math.tan(ra)
print('O {}valor digitado foi {} e o seu {}seno{} é {:.2f}'.format(tri, ang, cor1, cor0, sen))
print('O valor digitado foi {} e o seu {}cosseno{} é {:.2f}'.format(ang, cor2, cor0, con))
print('O valor digitado{} foi {} e a sua {}tangente{} é {:.2f}'.format(tri, ang, cor1, cor0, tan))

