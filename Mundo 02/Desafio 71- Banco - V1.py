
valor = int(input('Qual o valor do saque? '))
soma = valor
ced = 50
somaced = 0
while True:
    if soma >= ced:
        soma -= ced
        somaced += 1
    else:
        if somaced > 0:
            print(f'O total de {somaced} cedulas de {ced} R$')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        somaced = 0
        if soma == 0:
            break
print('Volte sempre.')

