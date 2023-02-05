nome = str(input('Digite o nome completo: ')).strip()
divi = nome.split()
pn = divi[0]
un = divi[len(divi)-1]
print('O primeiro nome é {}'.format(pn))
print('O último nome é {}'.format(un))

