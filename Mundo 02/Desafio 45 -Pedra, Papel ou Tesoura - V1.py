#Exercicio 01
'''numUm = int(input('Digite o Primeiro Valor: '))
numDois = int(input('Digite o Segundo Valor: '))
if numUm < 0 or numDois < 0:
    print('Digite Apenas Números Positivos')
elif numDois > numUm or numUm > numDois:
    print(f'Esse é o Maior Valor {numDois}')
elif numUm > numDois:
    print(f'Esse é o Maior Valor {numUm}')
else:
    print('Os Números são iguais')
'''
#Exercico 02
'''num = int(input('Digite um Valor Qualquer: '))
if num > 0:
    print(f'O Valor Digitado foi {num} e é Possitivo')
else:
    print(f'O Valor Digitado foi {num} e é Negativo')
'''
#Exercicio 03
'''letra = str(input('Digite Seu Sexo F/M: ')).strip().upper()[0]
if letra == 'F':
    print(f'A Letra Digitada foi {letra} De Femenino')
elif letra == 'M':
    print(f'A Letra Digitada foi {letra} de Masculino')
else:
    print(f'{letra} è invalida, Digite uma Opção valida')
'''
#Exercicio 04
'''vogal = str(input('Digite uma letra: ')).strip().upper()
if vogal in 'AEIOU':
    print(f'A Letra {vogal} é uma Vogal')
else:
    print(f'A Letra {vogal} é uma Consoante')
'''

#Exercicio 05
'''primeiraNota = float(input('Digite a sua Primeira Nota:'))
segundaNota = float(input('Digite a sua Segunda Nota: '))
media = (primeiraNota + segundaNota) / 2
if media == 10:
    print('Aluno Aprovado com Distinção')
elif media >= 7:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')
'''

#Exercico 06
'''num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))
if num1 > num2 and num1 > num3:
    print(f'Esse é o maior número {num1}')
if num2 > num1 and num2 > num3:
    print(f'Esse é o maior número {num2}')
if num3 > num2 and num3 > num1:
    print(f'Esse é o maior número {num3}')
if num1 == num2 and num2 == num3 and num1 == num3:
    print('Os números são iguais')
'''

#Exercicio 07
'''num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))
if num1 > num2 and num1 > num3:
    print(f'Esse é o maior número {num1}')
elif num2 > num1 and num2 > num3:
    print(f'Esse é o maior número {num2}')
elif num3 > num2 and num3 > num1:
    print(f'Esse é o maior número {num3}')
elif num1 == num2 and num2 == num3 and num1 == num3:
    print('Os números são iguais')
if num1 < num2 and num1 < num3:
    print(f'Esse é o menor número {num1}')
elif num2 < num3 and num2 < num1:
    print(f'Esse é o menor número {num2}')
elif num3 < num2 and num3 < num1:
    print(f'Esse é o menor número {num3}')
'''

#Exercicio 08
'''preco1 = float(input('Digite o Valor do Primeiro Produto: '))
preco2 = float(input('Digite o Valor do Segundo Produro: '))
preco3 = float(input('Digite o Valor do Terceiro Produto: '))
if preco1 < preco2 and preco1 < preco3:
    print(f'Esse é o Valor do Produto mais Barato {preco1:.2f}')
elif preco2 < preco3 and preco2 < preco1:
    print(f'Esse é o Valor do Produto mais Barato {preco2:.2f}')
else:
    print(f'Esse é o Valor do Produto mais Barato {preco3:.2f}')
'''

#Exercicio 09 consegui sem usar ifs
maior = medio = menor = 0
numero1 = int(input('Digite o Primeiro Valor: '))
numero2 = int(input('Digite o Segundo Valor: '))
numero3 = int(input('Digiteo Terceiro Valor: '))
if numero3 < numero1 > numero2:
    maior = numero1
    if menor < numero1 < medio:
        medio = numero1
    elif medio < numero1 < menor:
        menor = numero1
elif numero3 < numero2 > maior:
    maior = numero2
    if menor < numero2 < medio:
        medio = numero2
    elif medio < numero2 < menor:
        menor = numero2
elif numero3 > numero1 and numero3 > maior:
    maior = numero3
    if menor < numero3 < medio:
        medio = numero3
    elif medio < numero3 < menor:
        menor = numero3
print(maior)
print(medio)
print(menor)


#Exercicio 10
'''turno = str(input('Digite em qual turno voce estuda M/V/N:')).strip().lower()[0]
if turno == 'm':
    print('Boa Dia e Bons Estudos')
if turno == 'v':
    print('Boa Tarde e Bons Estudos')
if turno == 'n':
    print('Boa Noite e Bons Estudos, Cuidado ao Sair do Colégio.')
    '''

#Exercicio 11
'''salario = float(input('Digite o valor do seu salário: '))
porcentagem20 = salario * 20 / 100
porcentagem15 = salario * 15 / 100
porcentagem10 = salario * 10 / 100
porcentagem5 = salario * 5 / 100
aumento = salario + porcentagem20
aumento1 = salario + porcentagem15
aumento2 = salario + porcentagem10
aumento3 = salario + porcentagem5
if salario <= 280:
    print(f'O seu salário anterior era de {salario} com o novo aumento fica {aumento} um acressimo real de {porcentagem20}')
elif salario > 280 and salario < 700:
    print(f'O seu salário anteiror era de {salario} com o novo aumento fica {aumento1} um acressimo real de {porcentagem15}')
elif salario > 700 and salario < 1500:
    print(f'O seu salário anterior era de {salario} com o novo aumento fica {aumento2} um acressimo real de {porcentagem10}')
elif salario >= 1500:
    print(f'O seu salário anterior era de {salario} com o novo aumento fica {aumento3} um acressimo real de {porcentagem5}')'''

#Exercicio 12
'''horasTrabalhadas = int(input('Digite quantas horas voce trabalhou esse mes: '))
valorHorasTrabalhadas = int(input('Digite qual é valor da sua hora de trabalho: '))
salario = horasTrabalhadas * valorHorasTrabalhadas
salarioir = salario * 5 / 100
salarioinss = salario * 10 / 100
salariofgts = salario * 11 / 100
descontoCinco = salario * 5 / 100
descontoDez = salario * 10 / 100
descontoVinte = salario * 20 / 100
salarioLiquidoCinco = salario - salarioir - salarioinss
salarioLiquidoDez = salario - salarioir - salarioinss
salarioLiquidoVinte = salario - salarioir - salarioinss
if salario <= 900:
    print('O seu salário é insento de qualquer inmposto')
elif salario > 900 and salario <= 1500:
    print(f'(-) IR (5%) R${salarioir:5}')
    print(f'(-) INSS (10%) R${salarioinss:6}')
    print(f'(-) FGTS (11%) R${salariofgts:6}')
    print(f'Total desconto R${salarioir + salarioinss:6}')
    print(f'O seu salário bruto é de {salario} depois dos impostos o valor líquido é de {salarioLiquidoCinco}')
elif salario > 1500 and salario <= 2500:
    print(f'(-) IR (5%) R${salarioir:5}')
    print(f'(-) INSS (10%) R${salarioinss:6}')
    print(f'(-) FGTS (11%) R${salariofgts:6}')
    print(f'Total desconto R${salarioir + salarioinss:6}')
    print(f'O seu salário bruto é de {salario} depois dos impostos o valor líquido é de {salarioLiquidoDez} ')
else:
    print(f'(-) IR (5%) R${salarioir:5}')
    print(f'(-) INSS (10%) R${salarioinss:6}')
    print(f'(-) FGTS (11%) R${salariofgts:6}')
    print(f'Total desconto R${salarioir + salarioinss:6}')
    print(f'O seu salário bruto é de {salario} depois dos impostos o valor líquido é de {salarioLiquidoVinte}')
'''

#Exercicio 13
'''dias = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado')
numero = int(input('Digite um valor entre 1 e 7: '))
if numero == 1:
    print(dias[0])
elif numero == 2:
    print(dias[1])
elif numero == 3:
    print(dias[2])
elif numero == 4:
    print(dias[3])
elif numero == 5:
    print(dias[4])
elif numero == 6:
    print(dias[5])
elif numero == 7:
    print(dias[6])
else:
    print('Eu disse ente 1 e 7')'''

#Exercicio 14
'''nota1 = float(input('Digite sua Primeria Nota: '))
nota2 = float(input('Digite sua Segunda Nota: '))
soma = (nota1 + nota2) / 2
if soma > 9 and soma <= 10:
    print('Aprovado, A')
elif soma > 7.5 and soma <=9:
    print('Aprovado, B')
elif soma > 6 and soma <= 7.5:
    print('Aprovado, C')
elif soma > 4 and soma <= 6:
    print('Reprovado, D')
else:
    print('Reprovado, E')'''


#Exercicio 15
'''reta1 = float(input('Digite a Primeira Reta: '))
reta2 = float(input('Digite a Segunda Reta: '))
reta3 = float(input('Digite a Última Reta: '))
formam = reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2
trIsoscelis = reta1 == reta2 or reta2 == reta3 or reta3 == reta1
trEquilatero = reta1 == reta2 == reta3
trEscaleno = reta1 != reta2 != reta3
if formam and trIsoscelis:
    print('As Retas Formam um Triangulo Isosceles')
elif formam and trEquilatero:
    print('As Retas Formam um Triangulo Equilatero')
elif formam and trEscaleno:
    print('As Retas Formam um Triangulo Escaleno')
else:
    print('As Retas não Formam um triangulo')'''

