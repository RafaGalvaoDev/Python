listaNumero = []
for itens in range(5):
    num = int(input('Digite um Valor: '))
    if itens == 0 or num > listaNumero[-1]:
        listaNumero.append(num)
    else:
        posicao = 0
        while posicao < len(listaNumero):
            if num <= listaNumero[posicao]:
                listaNumero.insert(posicao, num)
                break
            posicao += 1
print(f'A Ordem dos Números Digitados é: {listaNumero}')
