from Minhas_Defs.Interface.Menu import *
from Minhas_Defs.Aquivos import *
from time import sleep


arquivo = 'DesafioFinal.txt'

if Existe(arquivo):
    print('O Arquivo Existe')
else:
    print('O Arquivo Não Existe')
    criar(arquivo)

while True:
    resposta = menu(['Mostrar Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 'Sair do Programa'])
    if resposta == 1:
        lendo(arquivo)
    elif resposta == 2:
        cabeçalho('Cadastrando Novos Dados')
        nome = str(input('Digite o Nome: '))
        idade = leiaint('Digite a Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Programa')
        break
    else:
        print('Opção Invalida. ')
        continue
    sleep(1.5)

