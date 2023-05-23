def escreva():
    texto = texto_Entrada
    if len(texto) == 1:
        print('_' * 2)
        print(f'{texto}')
        print('_' * 2)
    else:
        print('_' * len(texto) * 2)
        print(f' {texto}')
        print('_' * len(texto) * 2)

texto_Entrada = str(input('Digite Um Texto Qualquer: '))
escreva()
