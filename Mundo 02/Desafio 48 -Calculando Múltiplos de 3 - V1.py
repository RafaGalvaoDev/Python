soma = 0
contador = 0
for quinhetos in range(1, 501, 2):
    if quinhetos % 3 == 0:
        contador = contador + 1
        soma = soma + quinhetos
print('O valos dos {} intens foi {}'.format(contador, soma))
