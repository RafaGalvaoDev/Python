from emoji import emojize
cor0 = '\033[m'
cor1 = '\033[0;30;42m'
ci = emojize(':cityscape_at_dusk:')
cida = str(input('{}Digite o nome da cidade:{}{} '.format(cor1, cor0, ci))).strip()
mi = cida.lower()
comp = mi.startswith('santo')
print('{}A cidade tem o nome {}{}{}'.format(cor1, comp, cor0, ci))

