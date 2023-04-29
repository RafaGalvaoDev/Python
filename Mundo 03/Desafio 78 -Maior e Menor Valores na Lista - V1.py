listaNumeros = list()
maior = menor = 0
for valor in range(5):
    listaNumeros.append(int(input('Digite um Valor: ')))
    if valor == 0:
        maior = menor = listaNumeros[valor]
    else:
        if listaNumeros[valor] > maior:
            maior = listaNumeros[valor]
        elif listaNumeros[valor] < menor:
            menor = listaNumeros[valor]
for posicao, valor in enumerate(listaNumeros):
    if valor == maior:
        print(f'O maior {maior} na posicao {posicao+1}')
for posicao, valor in enumerate(listaNumeros):
    if valor == menor:
        print(f'O menor {menor} na posicao {posicao+1} ')
