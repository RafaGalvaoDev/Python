from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
cond = 0
while cond != 5:
    print('''Digite [1] para Somar\nDigite [2] para Múltiplicar\nDigite [3] para Maior\nDigite [4] para Novos Número\nDigite [5] para Sair''')
    cond = int(input('Digite aqui:'))
    if cond == 1:
        soma = n1 + n2
        print('A soma de {} + {} é igual a {}'.format(n1, n2, soma))
    elif cond == 2:
        mult = n1 * n2
        print('A múltiplicação de {} x {} é igual a {}'.format(n1, n2, mult))
    elif cond == 3:
        if n1 > n2:
            print('{} é o maior'.format(n1))
        else:
            print('{} é o maior'.format(n2))
    elif cond == 4:
        print('Digite os Novos Números')
        n1 = int(input('Digite o número: '))
        n2 = int(input('Digite o número: '))
    elif cond == 5:
        print('Desligando...')
    else:
        print('Número invalido, tente novamente')
    sleep(2.5)
print('Até a Proxima')
