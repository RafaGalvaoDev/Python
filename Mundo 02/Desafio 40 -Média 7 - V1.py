nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua nota foi {}, Você Foi Reprovado'.format(media))
elif media >= 7:
    print('Sua nota foi {}, Você Foi Aprovado'.format(media))
else:
    print('Sua nota foi {}, Você Ficou de Recuperação'.format(media))
