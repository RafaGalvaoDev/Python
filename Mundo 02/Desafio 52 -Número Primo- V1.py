num = int(input('Digite um número: '))
conta = 0
for cun in range(1, num + 1):
    if num % cun == 0:
        conta = conta + 1
if conta == 2:
        print('O valor digitado é um número primo')
else:
        print('O valor digitado não é um número primo')
