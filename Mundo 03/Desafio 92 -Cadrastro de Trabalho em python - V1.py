from datetime import date
ano = date.today().year
dados = {}
dados['nome'] = str(input('Digite Seu Nome: '))
dados['ano de nascimento'] = int(input('Digite Seu Ano de Nascimento: '))
dados['carteira'] = int(input('Digite o Número da Sua Carteira de Trabalho: (0 se não tiver) '))
dados['idade'] = ano - dados['ano de nascimento']
if dados['carteira'] != 0:
    dados['ano de contratação'] = int(input('Digite o Ano de Contratação: '))
    dados['salario'] = float(input('Digite o Valor do Seu Salario: '))
    dados['contribuição'] = ano - dados['ano de contratação']
    dados['ano aposentadoria'] = dados['ano de contratação'] + 35
    dados['idade aposentadoria'] = dados['ano aposentadoria'] - dados['ano de nascimento']

for k, v in dados.items():
    print(f'{k} tem o valor: {v}')

