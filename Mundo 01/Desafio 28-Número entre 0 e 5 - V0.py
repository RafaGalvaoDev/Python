from random import randint
from emoji import emojize
ace = emojize(':trophy:')
ero = emojize(':cross_mark:')
inp = emojize(':prohibited:')
cor0 = '\033[m'
cor1 = '\033[0;30;41m'
cor2 = '\033[0;30;42m'
cor3 = '\033[0;30;43m'
cor4 = '\033[4m'
print('Estou pensado num número entre 0 e 5: ')
print('Você consegui acertar qual é? ')
nu = int(input('Escolha um número: '))
ale = randint(0, 5)
if nu == ale:
    print('{}você {}acertou{}{}, parabéns{}{}'.format(cor2, cor4, cor0, cor0, ace, ace))
elif nu > 5:
    print('{}{}Eu disse {}entre 0 e 5{}!!{}{}'.format(inp, cor3, cor4, cor0, cor0, inp))
else:
    print('{}Você {}errou{}, tente outra vez{}{}{}{}'.format(cor1, cor4, cor0, cor0, ero, ero, ero))
