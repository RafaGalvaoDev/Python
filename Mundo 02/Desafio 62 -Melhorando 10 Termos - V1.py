termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
ptermo = termo
cont = 1
nume = 0
m = 10
while m != 0:
    nume = nume + m
    while cont <= nume:
        print('{}'.format(termo))
        termo = termo + razao
        cont = cont + 1
    m = int(input('Deseja ver mais quantos termos: '))
print('O total termos foram {}'.format(nume))
