c = m = 0
n = int(input('Digite um número e veja sua tabuada: '))
while n > 0:
    while c < 10:
       # n = int(input('Digite um número e veja sua tabuada: '))
        c += 1
        m = n * c
        print(f'A tabuada de {n} x {c} = {m}')
    c = 0
    n = int(input('Digite um novo valor: '))
print('Volte logo')
