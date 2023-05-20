time = list()
jogador = dict()
partidas = []
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o Nome do jogador: '))
    jogos = int(input(f'Digite Quantas partidas {jogador["Nome"]} Jogou: '))
    partidas.clear()
    for contador in range(0, jogos):
        partidas.append(int(input(f'Quantos Gols o Jogador {jogador["Nome"]} Marcou na Partida {contador+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total de Gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str(input('Dejesa Continuar? S/N: ')).strip().upper()[0]
        if resposta in 'SN':
            break
    if resposta == 'N':
        break
print('Cod: ', end='')
for i in jogador.keys():
    print(f'{i:<17}', end='')
print()
print('__'*40)
for k, v in enumerate(time):
    print(f'{k:>5} ', end='')
    for j in v.values():
        print(f'{str(j):<17}', end='')
    print()
while True:
    buscando = int(input('Quer Ver os Dados de Qual Jogador? (999 Para Sair): '))
    if buscando == 999:
        break
    elif buscando >= len(time):
        print('Tente Um Número Valido.')
    else:
        print(f'Você Escolheu o Jogador {time[buscando]["Nome"]}')
        for i, gols in enumerate(time[buscando]['Gols']):
            print(f'No Jogo {i+1} Fez {gols}')
        print('_'*36)
print('Termina aqui')
