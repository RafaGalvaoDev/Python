import emoji
preco = float(input('Digite o valor do produto: R$ '))
desconto = (preco * 5) / 100
novoPreco = preco - desconto
din = emoji.emojize(':money_with_wings:')
din1 = emoji.emojize(':money_bag:')
cor0 = '\033[m'
cor1 = '\033[4;30;42m'
cor2 = '\033[4;30;41m'
print('O {}valor do produto era {} R${} e com 5% de desconto {}passa a ser {}R${}{}'.format(cor2, preco, cor0, cor1, novoPreco, cor0, din))
print('Um {}desconto de {} R${}{}'.format(cor1, desconto, cor0, din1))

