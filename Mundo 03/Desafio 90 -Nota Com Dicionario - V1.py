aluno = dict()
aluno['Nome'] = str(input('Digite o Nome do Aluno: '))
aluno['Nota'] = float(input('Digite a Nota do Aluno: '))
print(f'O Nome do Aluno é {aluno["Nome"]}')
print(f'A Média do Aluno Foi {aluno["Nota"]}')
if aluno['Nota'] < 7:
    print('A Situação do aluno é Reprovado')
elif aluno['Nota'] >= 7:
    print('A Situação do aluno é Aprovado')
    
