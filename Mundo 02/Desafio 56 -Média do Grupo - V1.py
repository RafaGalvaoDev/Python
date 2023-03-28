somaIdade = 0
contandoIdade = 0
homemVelho = 0
nomeHomenVelho = ''
mulher = 0
for n in range(1, 5):
    nome = str(input('Digite o nome da pessoa número {}: '.format(n))).strip()
    idade = int(input('Digite a idade:'))
    sexo = str(input('Digite M/F: ')).strip().lower()
    somaIdade = somaIdade + idade
    if n == 1 and 'm' in sexo:
        homemVelho = idade
        nomeHomenVelho = nome
    if 'm' in sexo and idade > homemVelho:
        homemVelho = idade
        nomeHomenVelho = nome
    if 'f' in sexo and idade > 20:
        mulher = mulher + 1
contandoIdade = somaIdade / 4
print('A média das idades do grupo é {}'.format(contandoIdade))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomeHomenVelho, homemVelho))
print('Temos {} mulher com menos de 20 anos'.format(mulher))

