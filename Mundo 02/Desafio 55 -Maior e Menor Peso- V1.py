mapes = 0
mepes = 0
for n in range(1, 6):
    pessoa = float(input('Digite o peso da pessoa número {}: '.format(n)))
    if n == 1:
        mapes = pessoa
        mepes = pessoa
    else:
        if pessoa > mapes:
            mapes = pessoa
        if pessoa < mepes:
            mepes = pessoa
print('entre as {} pessoas temos o maior peso {}Kg e menor peso {}Kq'.format(n, mapes, mepes))

