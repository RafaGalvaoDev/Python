from emoji import emojize
ze = emojize(':Keycap_0:')
nu = emojize(':input_numbers:')
cor0 = '\033[m'
cor1 = '\033[0;30;47m'
num = int(input('Digite um número entre 0 e 9999{}: '.format(nu)))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('{}O número tem{} {} unidades{}'.format(cor1, nu, uni, cor0))
print('O número tem {} dezenas{}'.format(dez, nu))
print('{}O número tem{} {} centenas{}'.format(cor1, nu, cen, cor0))
print('O número tem {} milhares{}'.format(mil, nu))
