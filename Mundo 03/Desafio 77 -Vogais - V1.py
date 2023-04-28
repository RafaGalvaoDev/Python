palavras = ('arroz', 'casa', 'lugar', 'bolo', 'amendoim')
for itens in palavras:
    print(f'\nNa paralavra {itens} temos', end=' ')
    for letras in itens:
        if letras.lower() in 'aeiou':
            print(letras, end='')
