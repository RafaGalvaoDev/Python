from emoji import emojize
nome = str(input('Digite o nome completo: ')).strip()
mi = nome.lower()
miin = emojize(':input_latin_lowercase:')
ma = nome.upper()
main = emojize(':input_latin_uppercase:')
jun = nome.split()
qin = emojize(':input_numbers:')
div = jun[0]
jc = nome.replace(' ', '')
cont = jc.__len__()
cor0 = '\033[m'
cor1 = '\033[0;30;47m'
cor2 = '\033[0;30;43m'
print('O nome com todas as {}letras minusculas{}{} é: {}'.format(cor1, cor0, miin, mi))
print('O nome com todas as {}letras maiusculas{}{} é: {}'.format(cor2, cor0, main, ma))
print('O primeiro nome tem{}: {} letras'.format(qin, div.__len__()))
print('{}O nome tem {} letras{}{}'.format(cor1, cont, cor0, qin))



