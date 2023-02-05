frase = str(input('Digite uma frase: '))
eg = str.isupper(frase)
ep = str.islower(frase)
ts = str.isspace(frase)
print('{} <<-- Esta em maiscula: {}'.format(frase, eg))
print('{} <<-- Esta em minusculo: {}'.format(frase, ep))
print('{} <<-- Tem espaços: {}'.format(frase, ts))

