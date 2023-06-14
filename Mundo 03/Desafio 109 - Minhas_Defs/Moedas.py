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



