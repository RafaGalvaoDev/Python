def ficha(nome='Desconhecido', gols=0):
    if gols == 0 or gols > 1:
        print(f'O Jogador {nome} fez {gols} Gols no Campeonato')
    else:
        print(f'O Jogador {nome} fez {gols} Gol no Campeonato')


nome = str(input('Digite o Nome do Jogador: '))
gols = str(input(f'Digite Quantos gols o Jogador {nome} Marcou: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
