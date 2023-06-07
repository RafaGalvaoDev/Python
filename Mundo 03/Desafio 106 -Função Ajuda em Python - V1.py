colores = ('\033[0;41m', #0
            '\033[m', #1
            '\033[0;30;42m', #2
            )


def ajudando(entrar):
    help(entrar)


def cabeçalho(mensagem, cores=0):
    tamanho = len(mensagem)
    print(colores[cores], end='')
    print('_' * tamanho)
    print(mensagem)
    print('_' * tamanho)
    print(colores[1], end='')

entrada = ''
while True:
    cabeçalho('Sistema Python_Help', 0)
    entrada = str(input('Digite a Biblioteca: '))
    if entrada.upper() == 'TERMINAR':
        break
    else:
        ajudando(entrada)
cabeçalho('Acabou', 2)
