from emoji import emojize
import random
stu = emojize(':man_student:')
cor0 = '\033[m'
cor1 = '\033[0;30;47m'
cor2 = '\033[0;30;41m'
cor3 = '\033[0;30;42m'
cor4 = '\033[0;30;43m'
al1 = str(input('Digite o nome do {}primeiro aluno{}:{} '.format(cor1, stu, cor0))).strip()
al2 = str(input('Digite o nome do {}segundo aluno{}:{} '.format(cor2, stu, cor0))).strip()
al3 = str(input('Digite o nome do {}terceiro aluno{}:{} '.format(cor3, stu, cor0))).strip()
alu4 = str(input('Digite o nome do {}quarto aluno{}:{} '.format(cor4, stu, cor0))).strip()
lista = [al1, al2, al3, alu4]
esco = random.choice(lista)
print('O aluno que vai {}apagar{} o quadro é: {}'.format(cor1, cor0, esco))
