from Minhas_Defs import Moedas

numero = float(input('Digite Um Valor: '))
print(f'Aumentado 23% de {Moedas.moeda(numero)} é {Moedas.aumentar(numero, 23, True)}')
print(f'Diminuindo 15% de {Moedas.moeda(numero)} é {Moedas.diminuir(numero, 15, True)}')
print(f'O dobro de {Moedas.moeda(numero)} é {Moedas.dobro(numero, True)}')
print(f'A Metade de {Moedas.moeda(numero)} é {Moedas.metade(numero, True)}')
