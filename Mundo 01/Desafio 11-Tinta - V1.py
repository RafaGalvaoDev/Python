largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual é a altura da parede? '))
medida = largura * altura
tinta = medida / 2
print('A medida total da parede é {:.2f}'.format(medida))
print('É possivel usar apenas {:.2f} litros de tinta'.format(tinta))

