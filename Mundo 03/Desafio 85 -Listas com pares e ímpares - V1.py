listaDeListas = [[], []]
for contador in range(7):
    numero = int(input(f'Digite o {contador+1} Valor: '))
    if numero % 2 == 0:
        listaDeListas[0].append(numero)
        listaDeListas[0].sort()
    elif numero % 2 != 0:
        listaDeListas[1].append(numero)
        listaDeListas[1].sort()
print(f'Os Números pares foram {listaDeListas[0]}')
print(f'Os Números impares foram {listaDeListas[1]}')
