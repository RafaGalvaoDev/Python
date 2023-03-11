peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso // (altura * altura)
if imc <= 18.5:
    print('O seu imc é {}, Você esta abaixo do peso ideal'.format(imc))
elif imc > 18.5 and (imc <= 25):
    print('O seu imc é {}, Você esta no peso ideal'.format(imc))
elif imc > 25 and (imc <= 30):
    print('O seu imc é {}, Você esta com sobrepeso'.format(imc))
elif imc > 30 and (imc <= 40):
    print('O seu imc é {}, Você esta com obsidade'.format(imc))
else:
    print('O seu imc é {}, Você esta com obsidade mórbida'.format(imc))
