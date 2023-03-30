from random import randint
palpite = 0
print('Vamos jogar um jogo de advinhação?')
num = int(input('Digite um numero entre 1 e 10: '))
pensando = randint(1, 10)
while num != pensando:
    num = int(input('Você perdeu, Tente outra vez: '))
    palpite = palpite + 1
if num == pensando:
    print('Você ganhou, parabéns os seus palpites foram {}'.format(palpite+1))
