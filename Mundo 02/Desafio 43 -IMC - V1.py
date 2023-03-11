peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
aq = altura * altura
imc = peso // aq
if imc <= 18.5:
    print('O seu imc é {}'.format(imc))
    print('Você esta abaixo do peso ideal')
elif imc > 18.5 and (imc <= 25):
    print('O seu imc é {}'.format(imc))
    print('Você esta no peso ideal')
elif imc > 25 and (imc <= 30):
    print('O seu imc é {}'.format(imc))
    print('Você esta com sobrepeso')
elif imc > 30 and (imc <= 40):
    print('O seu imc é {}'.format(imc))
    print('Você esta com obsidade')
else:
    print('O seu imc é {}'.format(imc))
    print('Você esta com obsidade mórbida')
