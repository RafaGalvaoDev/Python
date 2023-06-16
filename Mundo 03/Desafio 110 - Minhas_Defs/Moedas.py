def aumentar(n=0, taxa=0, forma=False):
    n = n + (n * taxa / 100)
    return n if forma is False else moeda(n)


def diminuir(n=0, taxa=0, forma=False):
    n = n - (n * taxa / 100)
    return n if forma is False else moeda(n)


def dobro(n=0, forma=False):
    n *= 2
    return n if not forma else moeda(n)


def metade(n=0, forma=False):
    n = n / 2
    return n if not forma else moeda(n)


def moeda(n=0):
    n = f'R${n:.2f}'.replace('.', ',')
    return n


def resumo(n=0, taxa_Aumento=0, taxa_Diminuição=0):
    print('_' * 20)
    print('  Resumo do Valor: ')
    print('_' * 20)
    print()
    print('_' * 40)
    print(f'Aumentando {taxa_Aumento}% de {moeda(n)} é {aumentar(n, taxa_Aumento, True)}')
    print(f'Diminuindo {taxa_Diminuição}%  de {moeda(n)} é {diminuir(n, taxa_Diminuição, True)}')
    print(f'O Doblo de {moeda(n)} é {dobro(n, True)}')
    print(f'A medatade de {moeda(n)} é {metade(n, True)}')
    print('_' * 40)
