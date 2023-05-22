def titilo():
    print('_' * 35)
    print('     Calculando Área do terreno      ')
    print('_' * 35)



def area():
    largura = largura_Terreno
    comprimento = comprimento_Terreno
    area = largura * comprimento
    print('A área de um terreno')
    print(f'com {largura} X {comprimento} é de {area}M')


titilo()
largura_Terreno = float(input('Digite a Largura do Terreno: '))
comprimento_Terreno = float(input('Digite o Comprimento do Terreno: '))
area()
