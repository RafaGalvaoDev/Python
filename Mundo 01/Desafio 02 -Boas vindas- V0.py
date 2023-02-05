import emoji
nome = str(input('Qual é o seu nome? ')).strip()
semCor = '\033[m'
vermelho = '\033[4;31m'
verde = '\033[4;32m'
espadas = emoji.emojize(':crossed_swords:')
arma = emoji.emojize(':bow_and_arrow:')
invaders = emoji.emojize(':alien_monster:')
print('Bem vindo {}{}{}{}{} espero que esteja bem!!'.format(espadas, verde, nome, semCor, espadas))
print('{}{}{} a terra esta {}sendo atacada{} por monstros{}{} vindos do espaço profundo pegue sua arma{}{} e nos ajude!!'.format(verde, nome, semCor, vermelho, semCor, invaders, invaders, arma, arma))
