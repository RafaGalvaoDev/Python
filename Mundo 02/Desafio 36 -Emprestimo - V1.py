casa = float(input('Digite o valor total a pagar no imovel: '))
salario = float(input('Digite o valor total do seu salário: '))
anos = int(input('Digite por quantos anos pretende pagar pelo imovel: '))
mensal = anos * 12
prestacao = (casa / mensal)
print('O valor a pagar é {:.2f}R$'.format(prestacao))
if prestacao == (salario*30)/100:
    print('O valor pode ser pago.')
elif prestacao > (salario*30)/100:
    print('O valor não podera ser pago.')
else:
    print('O valor podera ser pago sem maiores problemas.')


