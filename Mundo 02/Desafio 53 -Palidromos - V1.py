frase = str(input('Digite uma frase: ')).strip().lower()
separacao = frase.split()
juntando = ''.join(separacao)
inverso = ''
for palavra in range(len(juntando)-1, -1, -1):
    inverso += juntando[palavra]
if juntando == inverso:
    print('A frase {} e seu inverso {} formam um palindromo'.format(juntando, inverso))
else:
    print('A frase {} e seu inverso {} não são um palidromo. '.format(juntando, inverso))
