r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
retas = r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r3
doisLados = r1 == r2 or r2 == r3 or r3 == r1
ladosIguais = r1 == r2 == r3
todosLados = r1 != r2 != r3
if retas and ladosIguais:
    print('As retas formam um triangulo')
    print('As retam forma um triangulo Equilátero')
elif retas and doisLados:
    print('As retas formam um triangulo')
    print('As retas formam um triangulo Isóscele')
elif retas and todosLados:
    print('As retas formam um triangulo')
    print('As retas forma um triangulo Escaleno')
else:
    print('As retas não formam um triangulo')
