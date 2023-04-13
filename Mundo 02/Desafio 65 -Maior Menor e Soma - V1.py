media = qdn = maior = menor = soma = 0
res = 's'
while res == 's':
    num = int(input('Digite um número: '))
    soma = soma + num
    qdn = qdn + 1
    if qdn == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Dejesa continuar S/N: ')).strip().lower()
media = soma / qdn
print('A quantidade de números digitados foi {} a media entre eles foi {} e a soma entre os números {}'.format(qdn, media, soma))
print('O maior número foi {} e o menor foi {}'.format(maior, menor))
