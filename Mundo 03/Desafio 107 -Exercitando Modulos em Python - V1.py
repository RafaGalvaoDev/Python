from Minhas_Defs import Moedas

numero = float(input('Digite Um Valor: '))
print(f'Aumentado 23% de {numero} é {Moedas.aumentar(numero, 23)}')
print(f'Diminuindo 15% de {numero} é {Moedas.diminuir(numero, 15)}')
print(f'O dobro de {numero} é {Moedas.moeda(Moedas.dobro(numero))}')
print(f'A Metade de {numero} é {Moedas.metade(numero)}')
