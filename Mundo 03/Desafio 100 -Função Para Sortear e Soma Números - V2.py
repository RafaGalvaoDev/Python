from random import randint
from time import sleep
lista_De_Pares = list()


def sorteio():
    for numero in range(0, 5):
        numero_Aleatorio1 = randint(0, 100)
        lista_De_Pares.append(numero_Aleatorio1)
    print('_' * 65)
    print('Sorteando Aleatoriamente 5 Números entre 0 e 100: ', end='')

    for valor in lista_De_Pares:
        print(f'{valor} ', end='')
        sleep(0.8)
    print()
    print('_' * 65)

def somarPar(soma=0):
    for valor in lista_De_Pares:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os Valores Pares de {lista_De_Pares} temos: ', end='')
    print(soma)
    print('_' * 65)

sorteio()
somarPar()
