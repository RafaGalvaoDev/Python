from emoji import emojize
ma = emojize(':black_large_square:')
me = emojize(':black_small_square:')
cor0 = '\033[m'
cor1 = '\033[7;30;43m'
cor2 = '\033[7;37;40m'
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
if num2 < num1 and num2 < num3:
    print('Esse é o {}menor{} número:{} {}'.format(cor2, me, cor0, num2))
elif num3 < num1 and num3 < num2:
    print('Esse é o {}menor{} número:{} {}'.format(cor2, me, cor0, num3))
else:
    print('Esse é o {}menor{} número:{} {}'.format(cor2, me, cor0, num1))
if num2 > num1 and num2 > num3:
    print('Esse é o {}maior{} número:{} {}'.format(cor1, ma, cor0, num2))
elif num3 > num1 and num3 > num1:
    print('Esse é o {}maior{} número:{} {}'.format(cor1, ma, cor0, num3))
else:
    print('Esse é o {}maior{} número:{} {}'.format(cor1, ma, cor0, num1))
