listaExpressao = []
valor = str(input('Digite Sua Expressão: '))
for iten in valor:
    if iten == '(':
        listaExpressao.append('(')
    elif iten == ')':
        if len(listaExpressao) > 0:
            listaExpressao.pop()
        else:
            listaExpressao.append(')')
            break
if len(listaExpressao) == 0:
    print(f'Sua Expressão {valor} é Valida.')
else:
    print(f'Sua Expressão {valor} Não é Valida.')

