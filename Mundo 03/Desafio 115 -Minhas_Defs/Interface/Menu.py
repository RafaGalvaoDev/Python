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


def linha(linhas=35):
    return "-" * linhas


def cabeçalho(mensagem):
    print(linha())
    print(mensagem.center(35))
    print(linha())


def menu(lista):
    cabeçalho('Menu Inicial')
    contador = 1
    for itens in lista:
        print(f'{contador} -- {itens}')
        contador += 1
    print(linha())
    escolha = leiaint('Digite Uma Opção: ')
    return escolha