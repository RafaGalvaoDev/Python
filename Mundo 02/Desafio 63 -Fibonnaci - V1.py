term = int(input('Digite o valor de termos que voce quer ver: '))
t1 = 0
t2 = 1
contador = 3
print('{} - {} - '.format(t1, t2), end='')
while contador <= term:
    t3 = t1 + t2
    print(' - {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador = contador + 1