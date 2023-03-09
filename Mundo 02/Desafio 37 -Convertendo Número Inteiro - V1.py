num = int(input('Digite um número inteiro: '))
es = int(input('Digite 1 para binário\nDigite 2 para octal\ndigite 3 para hexadecimal\nDigite a opção: '))
if es == 1:
    print('O valor digitado {} coresponde a {} em Binário'.format(num, bin(num)[2:]))
elif es == 2:
    print('O valor digitado {} coresponde a {} em Octal'.format(num, oct(num)[2:]))
elif es == 3:
    print('O valor digitado {} coresponde a {} em Hexadecimal'.format(num, hex(num)[2:]))
else:
    print('Voce só pode escolher entre 1, 2 ou 3.')

