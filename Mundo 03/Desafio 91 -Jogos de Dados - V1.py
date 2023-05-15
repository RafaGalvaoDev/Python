from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}
n = {}
for k, v in jogos.items():
    print(f'O {k} Tirou {v} nos Dados')
    sleep(0.7)
print('_'*50)
n = sorted(jogos.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(n):
    print(f'O {v[0]} em {i+1}° Lugar com {v[1]} Pontos')
    sleep(0.6)
