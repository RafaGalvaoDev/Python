s = cn = 0
print('Digite 999 para parar o programa')
n = int(input('Digite um número: '))
while True:
    while n != 999:
        cn += 1
        s = s + n
        n = int(input('Digite um número: '))
    if n == 999:
        print(f'A soma entre os números é {s} e a quantidade de digitados foi {cn}')
        break
