qdn = soma = num = 0
num = int(input('Digite um número ou 999 para parar:'))
while num != 999:
    qdn = qdn + 1
    soma = num + soma
    num = int(input('Digite um número ou 999 para parar:'))
print('A soma entre os números é {} e voce usou {} números'.format(soma, qdn))
