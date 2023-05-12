lista = []
while True:
    nome = str(input('Digite o Nome do Aluno: '))
    nota1 = float(input('Digite a Primeria Nota: '))
    nota2 = float(input('Digite a Segunda Nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    desejo = str(input('Deseja continuar S/N? ')).strip().upper()[0]
    if desejo in 'Nn':
        break
print(f'{"Numero":<4}{"Nome":>7}{"Media":>12}')
for item, alunoNome in enumerate(lista):
    print(f'{item:<4}{alunoNome[0]:>9}{alunoNome[2]:>12.2f}')
while True:
    escolha = int(input('De Qual Aluno Deseja Ver as Notas? (999) Para Finalizar: '))
    if escolha == 999:
        break
    elif escolha <= len(lista) - 1:
        print(f'Notas de {lista[escolha][0]} foram {lista[escolha][1]}')
