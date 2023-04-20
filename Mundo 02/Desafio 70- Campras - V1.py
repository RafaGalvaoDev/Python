soma = mil = menor = c = 0
barat = ''
while True:
    preco = float(input('Digite o valor do produto em R$: '))
    nomeProduto = str(input('Digite o nome do produto: ')).strip().upper()
    soma += preco
    c += 1
    if preco >= 1000:
        mil += 1
    if c == 1:
        menor = preco
        barat = nomeProduto
    else:
        if preco < menor:
            menor = preco
            barat = nomeProduto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Dejesa continuar? S/N: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O valor da sua compra foi {soma:.2f}')
print(f'{mil} proutos custaram 1000 R$ ou mais')
print(f'O produto mais barato foi {barat} custando {menor:.2f} R$')
