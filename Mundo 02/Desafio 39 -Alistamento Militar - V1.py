from datetime import date
data = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = data - ano
ali = 18 - idade
aliIm = idade - 18
print('Estamos no ano de {}, sua idade é {} anos'.format(data, idade))
if idade <= 17:
    print('Ainda falta {} anos para seu alistamento'.format(ali))
elif idade == 18:
    print('Esta na idade de alistamento')
else:
    print('Já passou {} anos para o seu alistamento, apressente-se imediatamente'.format(aliIm))
