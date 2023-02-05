salario = float(input('Digite o seu salário R$: '))
au15 = (salario * 15) / 100
au10 = (salario * 10) / 100
novoSal15 = salario + au15
novoSal10 = salario + au10
if salario > 1250:
    print('O novo salário é de {:.2f}R$'.format(novoSal10))
    print('Um aumento de {:.2f}R$'.format(au10))
else:
    print('O novo salário é de {:.2f}'.format(novoSal15))
    print('Um aumento de {:.2f}'.format(au15))

