listaNumero = []
while True:
    numero = int(input('Digite um Valor: '))
    desejaContinuar = str(input('Você Deseja Continuar S/N? ')).strip().upper()[0]
    if numero not in listaNumero:
        listaNumero.append(numero)
        print('O número foi Adicionado a lista.')
    else:
        print('Número já inserido tente outro.')
    while desejaContinuar not in 'snSN':
        print('Solicitação Invalida:')
        desejaContinuar = str(input('Você Quer continuar S/N?? '))
    if desejaContinuar in 'N':
        print('=-=-='*12)
        print(f'Os números digitados foram {listaNumero}')
        listaNumero.sort()
        print('=-=-='*12)
        print(f'Os numeros em ordem crescente é {listaNumero}')
        break
