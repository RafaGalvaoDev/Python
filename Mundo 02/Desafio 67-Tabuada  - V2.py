from time import sleep
c = m = 0
n = int(input('Digite um número e veja sua tabuada: '))
while c < 10:
    if n <= 0:
        print('Volte logo')
        break
    c += 1
    m = n * c
    print(f'A tabuada de {n:2} X {c:2} = {m:2}')
    if c == 10:
        c = 0
        c += 1
        n = int(input('Digite um Novo Número:'))
        m = n * c
        sleep(1)
        print(f'A tabuada de {n:2} X {c:2} = {m:2}')
