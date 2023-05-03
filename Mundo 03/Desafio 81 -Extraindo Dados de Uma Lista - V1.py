listaNumero = list()
while True:
    listaNumero.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar S/N? ')).strip().lower()[0]
    while continuar not in 'sSnN':
        print('Indicativa Invalida, Tente Novamente.')
        continuar = str(input('Deseja Continuar S/N? '))
    if continuar == 'n':
        print(f'Foram Digitado {len(listaNumero)} Elementos')
        listaNumero.sort(reverse=True)
        print(f'Os Valores Digitados em Ordem Decresente é {listaNumero}')
        if listaNumero.count(5) == 0:
            print('O Número 5 Não Aparece na Lista.')
        elif listaNumero.count(5) == 1:
            print(f'O Número 5 Aparece {listaNumero.count(5)} Vez')
        else:
            print(f'O Número 5 Aparece {listaNumero.count(5)} Vezes')
        break
