from emoji import emojize
es = emojize(':open_book:')
nome = str(input('Digite o nome completo:{} '.format(es))).strip()
nm = nome.lower()
ns = 'silva' in nm
cor0 = '\033[m'
cor1 = '\033[4;30;44m'
print('{}O nome digitado tem silva:{} {}{} '.format(cor1, cor0, ns, es))
