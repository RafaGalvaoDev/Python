listapreco = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'MOchila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for itens in range(0, len(listapreco)):
    if itens % 2 == 0:
        print(f'{listapreco[itens]:.<20}', end='')
    if itens % 2 == 1:
        print(f'R${listapreco[itens]:>6.2f}')
