num = int(input('Digite um número entre 0 e 9999: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print('O número tem {} unidades'.format(uni))
print('O número tem {} dezenas'.format(dez))
print('O número tem {} centenas'.format(cen))
print('O número tem {} milhares'.format(mil))

