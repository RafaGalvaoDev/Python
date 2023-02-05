preco = float(input('Digite o valor do produto: '))
desconto = (preco * 5) / 100
novoPreco = preco - desconto
print('O valor do produto é {:.2f}R$'.format(preco))
print('O valor com 5% de desconto é {:.2f}R$'.format(novoPreco))
print('Um desconto de {:.2f}R$'.format(desconto))

