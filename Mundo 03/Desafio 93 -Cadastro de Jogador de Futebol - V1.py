jogador = dict()
partidas = []
jogador['Nome'] = str(input('Digite o Nome do jogador: '))
jogos = int(input(f'Digite Quantas partidas {jogador["Nome"]} Jogou: '))
for contador in range(0, jogos):
    partidas.append(int(input(f'Quantos Gols o Jogador {jogador["Nome"]} Marcou na Partida {contador+1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total de Gols'] = sum(partidas)
print('_'*50)
for k, v in jogador.items():
    print(f'O {k} tem {v}')
print('_'*50)
print(f'O Jogador {jogador["Nome"]} Jogou em {jogos} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'Na Partida {i+1}, Fez {v} Gols')
print(f'Um total de {jogador["Total de Gols"]} Marcados')
