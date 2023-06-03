def leiaint(mensagem):
    certo = False
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            certo = True
        else:
            print('Digite Um Número Valido.')
        if certo:
            break
    return valor


numero = leiaint('Digite Um Número: ')
print(f'Você digitou: {numero}')
