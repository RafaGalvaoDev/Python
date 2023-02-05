import emoji
pincel = emoji.emojize(':paintbrush:')
parede = emoji.emojize(':brick:')
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
medida = largura * altura
tinta = medida / 2
cor0 = '\033[m'
cor1 = '\033[4;30;42m'
cor2 = '\033[0;30;44m'
print('A medida {}total da parede{} é {:.2f}{} metros'.format(cor1, parede, medida, cor0))
print('Para pintar{} a {}parede você usara {:.2f} litros{} de tinta.'.format(pincel, cor2, tinta, cor0))

