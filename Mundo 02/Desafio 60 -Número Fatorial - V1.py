fatorial = 1
n = 1
num = int(input('Digite um número: '))
while num >= n:
    fatorial = fatorial * n
    n = n + 1
    print('O fatorial de {} é {}'.format(num, fatorial))
