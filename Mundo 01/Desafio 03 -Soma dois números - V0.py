import emoji
um = emoji.emojize(':keycap_1:')
dois = emoji.emojize(':keycap_2:')
n1 = int(input('Digite o primeiro {} número: '.format(um)))
n2 = int(input('Digite o segundo {} número: '.format(dois)))
mais = emoji.emojize(':plus:')
soma = n1 + n2
verde = '\033[4;32m'
vermelho = '\033[4;31m'
ciano = '\033[4;32m'
semCor = '\033[m'
print('A soma {} entre {}{}{} e {}{}{} é igual a {}{}{}'.format(mais, verde, n1, semCor, vermelho, n2, semCor, ciano, soma, semCor))

