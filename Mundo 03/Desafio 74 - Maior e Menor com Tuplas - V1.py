from random import randint
numeros1 = randint(1, 20)
numeros2 = randint(1, 20)
numeros3 = randint(1, 20)
numeros4 = randint(1, 20)
numeros5 = randint(1, 20)
tupla = (numeros1, numeros2, numeros3, numeros4, numeros5)
print('Os valores sortedos foi: ', end='')
for itens in tupla:
    print(f'{itens}', end=' ')
print(f'\nO maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')
