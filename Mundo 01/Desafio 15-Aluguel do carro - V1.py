km = float(input('Quantos quilometros o carro percoreu: '))
dia = int(input('Por quantos dias usou o carro: '))
vd = dia * 60
vkm = (km * 0.15)
soma = vkm + vd
print('O valor a pagar por {} dias é de {}'.format(dia, vd))
print('O valor a pagar por {} km é de {}'.format(km, vkm))
print('Um total de {}'.format(soma))
