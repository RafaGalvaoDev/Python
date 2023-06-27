from Minhas_Defs.Interface.Menu import cabeçalho


def Existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Ocorreu Um Erro ao Criar o Arquivo {nome}')
    else:
        print(f'O Arquivo {nome} foi Criado')


def lendo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao Tentar Ler o Arquivo')
    else:
        cabeçalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.strip(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<10} {dado[1]:>5} Anos')
    finally:
        a.close()


def cadastrar(arquivo, nome='Desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um Erro ao Abrir o Arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao Adicionar Novos Dados')
        else:
            print('Dados Adicionados')
            a.close()

