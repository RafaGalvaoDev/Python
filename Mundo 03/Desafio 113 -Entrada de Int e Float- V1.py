def leiaint(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except(ValueError, TypeError):
            print('Ocorreu um Erro de Entrada, Digite Um Número INTEIRO.')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mO Usuário Interrompeu a Entrada de Dados.\033[m')
            return 0
        else:
            return numero


def leiafloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except(ValueError, TypeError):
            print('Ocorreu um ERRO de Entrada, Digite Um Número Real.')
            continue
        except KeyboardInterrupt:
            print('\033[0;30;41mO Usuário Interrompeu a Entrada de Dados.\033[m')
            return 0
        else:
            return numero


interger = leiaint('Digite Um Número Inteiro: ')
floating = leiafloat('Digite um Número Real: ')
print(f'Número Inteiro Digitado foi: {interger}')
print(f'Número Real Digitado foi: {floating}')

