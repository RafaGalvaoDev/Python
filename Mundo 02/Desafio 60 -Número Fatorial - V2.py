num = int(input('Digite um valor: '))
print('Fatorial {}!'.format(num))
contador = num
fatorial = 1
while contador > 0:
    print('{}'.format(contador), end='')
    print(' X ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador
    contador = contador - 1
print('{}'.format(fatorial))
