from math import sqrt
num = int(input('Digite um número: '))
d = num * 2
t = num * 3
r = sqrt(num)
print('O número digitado foi {} e o seu dobro é {}'.format(num, d))
print('O número digitado foi {} e o seu triplo é {}'.format(num, t))
print('O número digitado foi {} e a sua raiz é {:.2f}'.format(num, r))

