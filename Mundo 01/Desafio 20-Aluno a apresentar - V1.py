import random
alu1 = str(input('Digite o nome do primeiro aluno: ')).strip()
alu2 = str(input('Digite o nome do segundo aluno: ')).strip()
alu3 = str(input('Digite o nome do terceiro aluno: ')).strip()
alu4 = str(input('Digite o nome do quarto aluno: ')).strip()
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print('O primeiro aluno a apresentar será: {}'.format(lista[0]))
print('O segundo aluno a apresentar será: {}'.format(lista[1]))
print('O terceiro aluno a apresentar será: {}'.format(lista[2]))
print('O quarto aluno a apresentar será: {}'.format(lista[3]))
