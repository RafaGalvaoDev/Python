from random import randint
palpite = 0
print('Vamos jogar um jogo? \nTente acertar o número que pensei\nO número esta entre 0 e 10')
pensador = randint(0, 10)
num = int(input('Digite o número: '))
while num != pensador:
    num = int(input('Tente novamente: '))
    palpite += 1
    if num > pensador:
        print('O número que eu pensei é menor do que {}'.format(num))
    elif num < pensador:
        print('O númeor que eu pensei é maior do que {}'.format(num))
print('Voce ACERTOU PARABÉNS, voce chutou {} vezes'.format(palpite+1))
