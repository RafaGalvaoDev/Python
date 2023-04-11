qdn = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número ou 999 para parar:'))
    qdn = qdn + 1
    soma = num + soma
print('A soma entre os números é {} e voce usou {} números'.format(soma-999, qdn-1))
