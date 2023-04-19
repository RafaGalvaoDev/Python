from datetime import date
ano = date.today().year
con = h = m = 0
while True:
    anoNascimento = int(input('Digite o ano de nascimento: '))
    mf = ' '
    idade = ano - anoNascimento
    while mf not in 'MF':
        mf = str(input('Digite M/F: ')).strip().upper()
    if idade >= 18:
       con += 1
    if mf == 'M':
        h += 1
    if mf == 'F' and idade < 20:
        m += 1
    sn = ' '
    while sn not in 'NS':
        sn = str(input('Deseja continuar N/S: ')).strip().upper()
    if sn == 'N':
        break
print(f'{con} é maior de idade')
print(f'Temos {h} Homens')
print(f'E são {m} mulheres com idade inferior a 20 anos')
