from random import randint
print('Estou pensado num número entre 0 e 5: ')
print('Você consegui acertar qual é? ')
nu = int(input('Escolha um número: '))
ale = randint(0, 5)
if nu == ale:
    print('você acertou, parabéns')
elif nu > 5:
    print('Eu disse entre 0 e 5!!')
else:
    print('Você errou, tente outra vez')
