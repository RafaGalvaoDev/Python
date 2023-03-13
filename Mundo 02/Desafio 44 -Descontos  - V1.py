preço = float(input('Digite o valor do produto R$: '))
dez = (preço * 10) / 100
cinco = (preço * 5) / 100
vinte = (preço * 20) / 100
nu1 = int(input("""Digite 1 para pagar avista no dinheiro ou cheque
Digite 2 para pagar avista no cartão
Digite 3 para pagar em até 2x no cartão
Digite 4 para pagar em 3x ou mais no cartão: """))

if nu1 == 1:
    print('Você selecionou avista no dinheiro ou cheque')
    print('O valor a pagar é de {:.2f}'.format(preço-dez))
elif nu1 == 2:
    print('Você selecionou avista no cartão')
    print('O valor a pagar é de {:.2f}'.format(preço-cinco))
elif nu1 == 3:
    print('Você selecionou em até 2x no cartão')
    print('O valor a pagar é de {:.2f}'.format(preço))
else:
    print('Você selecionou em até 3x ou mais no cartão')
    print('O valor a pagar é de {:.2f}'.format(preço+vinte))
