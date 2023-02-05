from emoji import emojize
cor0 = '\033[m'
cor1 = '\033[4;30;41m'
cor2 = '\033[4;30;42m'
cg = emojize(':thermometer:')
graus = float(input('Digite o valor da {}temperatura em graus:{}{} '.format(cor2, cor0, cg)))
f = (graus * 1.8) + 32
print('{}A temperatura{} de {} graus{} celsius é igual a {:.2f} graus fahrenheit'.format(cor1, cor0, graus, cg, f))
