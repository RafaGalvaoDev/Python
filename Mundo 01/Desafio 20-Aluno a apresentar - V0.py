import random
from emoji import emojize
stu = emojize(':man_student:')
p = emojize(':keycap_1:')
s = emojize(':keycap_2:')
t = emojize(':keycap_3:')
q = emojize(':keycap_4:')
cor0 = '\033[m'
cor1 = '\033[0;30;41m'
cor2 = '\033[4;30;47m'
cor3 = '\033[0;30;42m'
cor4 = '\033[0;30;44m'
alu1 = str(input('Digite o nome do {}primeiro aluno:{}{} '.format(cor1, cor0, stu))).strip()
alu2 = str(input('Digite o nome do {}segundo aluno:{}{} '.format(cor2, cor0, stu))).strip()
alu3 = str(input('Digite o nome do {}terceiro aluno:{}{} '.format(cor3, cor0, stu))).strip()
alu4 = str(input('Digite o nome do {}quarto aluno:{}{} '.format(cor4, cor0, stu))).strip()
lista = [alu1, alu2, alu3, alu4]
random.shuffle(lista)
print('O {}primeiro aluno a {}apresentar será: {}{}'.format(p, cor1, lista[0], cor0))
print('O {}segundo aluno a {}apresentar será: {}{}'.format(s, cor2, lista[1], cor0))
print('O {}terceiro aluno a {}apresentar será: {}{}'.format(t, cor3, lista[2], cor0))
print('O {}quarto aluno a {}apresentar será: {}{}'.format(q, cor4, lista[3], cor0))

