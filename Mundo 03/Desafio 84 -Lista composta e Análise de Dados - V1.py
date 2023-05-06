nomePeso = []
dados = []
pesado = leve = contador = 0
while True:
    dados.append(str(input('Digite o Nome: ')))
    dados.append(float(input('Digite o Peso: ')))
    if len(nomePeso) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        elif dados[1] < leve:
            leve = dados[1]
    nomePeso.append(dados[:])
    dados.clear()
    contador += 1
    desejaContinuar = str(input('Dejesa Continuar S/N? ')).strip().upper()[0]
    if desejaContinuar in 'N':
        break
print(f'{contador} Pessoas Cadastradas')
print(f'O maior peso foi de {pesado}Kg.', end='')
for pessoa in nomePeso:
    if pessoa[1] == 100:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f'O menor peso foi de {leve}Kg.', end='')
for pessoa in nomePeso:
    if pessoa[1] == 70:
        print(f'[{pessoa[0]}] ', end='')
