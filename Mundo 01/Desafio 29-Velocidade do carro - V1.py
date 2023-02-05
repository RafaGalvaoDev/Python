km = float(input('Digite a velocidade do carro: Km '))
mut = (km - 80) * 7
print('A sua velocidade foi de {}KM/H'.format(km))
if km > 80:
    print('Você foi multado o valor a ser pago é de {:.2f}R$'.format(mut))
else:
    print('Continue digirindo, com segurança')

