povo = []
pessoas = {}
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Digite o Sexo F/M: ')).strip().upper()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Tente Outra Vez')
    pessoas['Idade'] = int(input('Digite a Idade: '))
    soma += pessoas['Idade']
    povo.append(pessoas.copy())
    while True:
        resposta = str(input('Deseja Continuar? S/N: ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Tente SIM ou NÃO')
    if resposta == 'N':
        break
print(f'Temos {len(povo)} Pessoas')
media = soma / len(povo)
print(f'A Média das Idades é de {media:3.2f} Anos')
print('As Mulheres foram: ', end='')
for pessoas in povo:
    if pessoas['Sexo'] == 'F':
      print(f'{pessoas["Nome"]} ', end='')
print()
print('Pessoas Acima da média de Idade')
for pessoas in povo:
    if pessoas['Idade'] >= media:
        for k, v in pessoas.items():
            print(f'{k} == {v}; ', end='')
print('Fim')
