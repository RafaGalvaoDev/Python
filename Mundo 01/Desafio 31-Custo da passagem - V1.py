passagem = int(input('Digite quantos quilometros pretende viajar: Km '))
valor1 = passagem * 0.50
valor2 = passagem * 0.45
if passagem <= 200:
    print('Sua viagem é de {}Km'.format(passagem))
    print('O valor a ser pago é de {:.2f}'.format(valor1))
else:
    print('Sua viagem é de {}Km'.format(passagem))
    print('O valor a ser pago é de {:.2f}R$'.format(valor2))
