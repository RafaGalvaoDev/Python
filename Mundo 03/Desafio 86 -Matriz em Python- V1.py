matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = somaLista = 0
for n in range(3):
    for item in range(3):
        matriz[n][item] = int(input('Digite Um valor: '))
for n in matriz:
    for item in n:
        print([item], end=' ')
        if item == 3 or item == 6:
            print()
for n in range(3):
    somaLista += matriz[n][2]
    for item in range(3):
        if matriz[n][item] % 2 == 0:
            soma += matriz[n][item]
for item in range(3):
    if item == 0:
        maior = matriz[1][item]
    elif matriz[1][item] > maior:
        maior = matriz[1][item]
print()
print(f'A Soma entre os números pares é {soma}')
print(f'A soma da coluna 3 é {somaLista}')
print(f'O maior número da linha 2 é {maior}')
