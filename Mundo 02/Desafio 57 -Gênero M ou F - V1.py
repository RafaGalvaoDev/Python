sex = str(input('Digite o seu sexo F/M: ')).strip().lower()
while sex != 'm' and sex != 'f':
    sex = str(input('Tente Novamente: ')).strip().lower()
if sex == 'f':
    print('O seu sexo é Feminino')
elif sex == 'm':
    print('O seu sexo é Masculino')

