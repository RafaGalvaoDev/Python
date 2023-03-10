from datetime import date
data = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = data - ano
if idade <= 9:
    print('Sua idade é {}, Você esta na categoria Mirim'.format(idade))
elif idade <= 14:
    print('Sua idade é {}, Você esta na categoria Infantil'.format(idade))
elif idade <= 19:
    print('Sua idade é {}, Você esta na categoria Junior'.format(idade))
elif idade <= 20:
    print('Sua idade é {}, Você esta na categoria Sênior'.format(idade))
else:
    print('Sua idade é {}, Você esta na categoria Master'.format(idade))

