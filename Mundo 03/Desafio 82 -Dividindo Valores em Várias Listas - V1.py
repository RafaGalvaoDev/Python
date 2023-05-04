listaNumeros = []
listaPar = []
listaImpa = []
while True:
    numero = int(input('Digite um Valor: '))
    continuar = str(input('Deseja Continuar S/N? ')).strip().upper()[0]
    while continuar not in 'sSnN':
        print('Indicativa Infalida, Tente Novamente.')
        continuar = str(input('Deseja Continuar S/N? ')).strip().upper()[0]
    if numero not in listaNumeros:
        listaNumeros.append(numero)
    while numero in listaNumeros:
        if numero % 2 == 0 not in listaNumeros:
            listaPar.append(numero)
            break
        elif numero % 2 != 0 not in listaNumeros:
            listaImpa.append(numero)
            break
    if continuar in 'nN':
        print(f'A lista dos Números Digitado é {listaNumeros}')
        print(f'A lista com os Números Pares é {listaPar}')
        print(f'A lista com os Números Impares é {listaImpa}')
        break
