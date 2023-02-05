from emoji import emojize
cor0 = '\033[m'
cor1 = '\033[0;30;41m'
cor2 = '\033[0;30;42m'
cor3 = '\033[4m'
p = emojize(':keycap_1:')
u = emojize(':keycap_0:')
nome = str(input('Digite o nome completo: ')).strip()
divi = nome.split()
pn = divi[0]
un = divi[len(divi)-1]
print('{}O primeiro{} nome é {}{}{}{}'.format(cor2, p, cor3, pn, cor0, cor0))
print('{}O último{} nome é {}{}{}{}'.format(cor1, u, cor3, un, cor0, cor0))

