from random import randint
print('Vamos jogar um joguinho de par ou impa')
cou = 0
while True:
    nu = int(input('Digite um valor: '))
    com = randint(1, 10)
    soma = com + nu
    paip = ' '
    while paip not in 'PI':
        paip = str(input('Digite P/I: ')).strip().upper()
    print(f'O valor escolhido foi {nu}, o computador escolheu {com}, a soma é {soma} ', end='')
    print('Deu par' if soma % 2 == 0 else 'Deu impa')
    if paip == 'P':
        if soma % 2 == 0:
            print('Você ganhou')
            cou += 1
        else:
            print('Você perdeu.')
            break
    elif paip == 'I':
        if soma % 2 == 1:
            print('Você ganhou')
            cou += 1
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {cou} vezes')
