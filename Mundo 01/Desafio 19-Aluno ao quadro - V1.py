import random
alu1 = str(input('Digite o nome do primeiro aluno: ')).strip()
alu2 = str(input('Digite o nome do segundo aluno: ')).strip()
alu3 = str(input('Digite o nome do terceiro aluno: ')).strip()
alu4 = str(input('Digite o nome do quarto aluno: ')).strip()
lista = [alu1, alu2, alu3, alu4]
esco = random.choice(lista)
print('O aluno que vai apagar o quadro é: {} '.format(esco))

