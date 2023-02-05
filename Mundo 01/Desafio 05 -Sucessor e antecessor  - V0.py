import emoji
numero = int(input('Digite um número inteiro Qualquer: '))
ant = numero - 1
suc = numero + 1
vant = emoji.emojize(':baby_symbol:')
vsuc = emoji.emojize(':wheelchair_symbol:')
verde = '\033[4;32m'
vermelho = '\033[4;31m'
semCor = '\033[m'
print('O número digitado foi {} o seu {}antecessor{} {} é {} e seu {}sucessor{} {} é {}'.format(numero, verde, semCor, vant, ant, vermelho, semCor, vsuc, suc))

