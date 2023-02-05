num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
if num2 < num1 and num2 < num3:
    print('Esse é o menor número {}'.format(num2))
elif num3 < num1 and num3 < num2:
    print('Esse é o menor número {}'.format(num3))
else:
    print('Esse é o menor número {}'.format(num1))
if num2 > num1 and num2 > num3:
    print('Esse é o maior número {}'.format(num2))
elif num3 > num1 and num3 > num1:
    print('Esse é o maior número {}'.format(num3))
else:
    print('Esse é o maior número {}'.format(num1))
