from emoji import emojize
cor0 = '\033[m'
cor1 = '\033[0;30;42m'
cor2 = '\033[0;30;43m'
din = emojize(':money_bag:')
din1 = emojize(':dollar_banknote:')
salario = float(input('Digite o seu salário{} R$: '.format(din)))
au15 = (salario * 15) / 100
au10 = (salario * 10) / 100
novoSal15 = salario + au15
novoSal10 = salario + au10
if salario > 1250:
    print('{}O novo salário{} é de {:.2f}R$'.format(cor1, cor0, novoSal10))
    print('{}Um aumento{} de {:.2f}R${}{}'.format(cor2, cor0, au10, din1, din1))
else:
    print('{}O novo salário{} é de {:.2f}'.format(cor2, cor0, novoSal15))
    print('{}Um aumento{} de {:.2f}{}{}'.format(cor1, cor0, au15, din1, din1))
