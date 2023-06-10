from Minhas_Defs import Moedas

numero = float(input('Digite Um Valor: '))
print(f'Aumentado 23% de {Moedas.moeda(numero)} é {Moedas.moeda(Moedas.aumentar(numero, 23))}')
print(f'Diminuindo 15% de {Moedas.moeda(numero)} é {Moedas.moeda(Moedas.diminuir(numero, 15))}')
print(f'O dobro de {Moedas.moeda(numero)} é {Moedas.moeda(Moedas.dobro(numero))}')
print(f'A Metade de {Moedas.moeda(numero)} é {Moedas.moeda(Moedas.metade(numero))}')
