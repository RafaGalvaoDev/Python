import emoji
cor0 = '\033[m'
cor1 = '\033[4;30;42m'
cor2 = '\033[0;30;43m'
cd = emoji.emojize(':money_bag:')
dc = emoji.emojize(':money_with_wings::money_with_wings:')
cc = emoji.emojize(':dinheiro-mouth_face:')
salario = float(input('Digite o valor do {}seu salário:{}{} '.format(cor1, cd, cor0)))
acre = (salario * 15) / 100
novoSalario = salario + acre
print('O valor de seu salário hoje é {}R$ com o acressimo de 15% {}passa a ser {}R${}{}'.format(salario, cor2,novoSalario, dc, cor0))
print('{}Um acressimo de {}R${}{}'.format(cor1, acre, cd, cor0))
