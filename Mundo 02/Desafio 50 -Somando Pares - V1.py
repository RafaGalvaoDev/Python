soma = 0
contador = 0
for s in range(6):
    w = int(input('Digite um número:'))
    if w % 2 == 0:
        soma = soma + w
        contador = contador +1
print('A soma dos {} números pares é {}'.format(contador, soma))
