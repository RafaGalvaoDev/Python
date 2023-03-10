from datetime import date
data = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = data - ano
if idade <= 9:
    print('Sua idade é {}'.format(idade))
    print('Você esta na categoria Mirim')
elif idade <= 14:
    print('Sua idade é {}'.format(idade))
    print('Você esta na categoria Infantil ')
elif idade <= 19:
    print('Sua idade é {}'.format(idade))
    print('Você esta na categoria Junior')
elif idade <= 25:
    print('Sua idade é {}'.format(idade))
    print('Você esta na categoria Sênior')
else:
    print('Sua idade é {}'.format(idade))
    print('Você esta na categoria Master')
