from random import randint
from time import sleep
lista = []
listaJogos = []
contador = 0
total = 1
quantidade = int(input('Digite quantos números de jogos quer: '))
while total <= quantidade:
    contador = 0
    while True:
        numeroAleatorio = randint(1, 60)
        if numeroAleatorio not in lista:
            lista.append(numeroAleatorio)
            contador += 1
        if contador == 6:
            break
    lista.sort()
    listaJogos.append(lista[:])
    lista.clear()
    total += 1
if quantidade == 1:
    print(f'Sorteando {quantidade} jogo')
else:
    print(f'Sorteando {quantidade} Jogos')
for n, l in enumerate(listaJogos):
    print(f'Jogo número {n+1}: {l}')
    sleep(0.7)
