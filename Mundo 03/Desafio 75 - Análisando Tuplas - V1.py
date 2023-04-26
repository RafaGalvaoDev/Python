numero = (int(input('Digite um número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite o último número: ')))
nove = numero.count(9)
print(f'O número 9 aparece {nove} vezes')
if 3 in numero:
    print(f'O número 3 aprece primeiro na posição {numero.index(3)+1}')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares foram: ', end='')
for itens in numero:
    if itens % 2 == 0:
        print(itens, end=' ')
