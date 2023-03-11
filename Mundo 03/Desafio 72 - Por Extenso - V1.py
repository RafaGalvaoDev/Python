numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quadro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'doze', 'Treze', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        break
    print('Tente um número entre 0 e 20:')   
print(f'Voce digitou {numeros[num]}')
          
