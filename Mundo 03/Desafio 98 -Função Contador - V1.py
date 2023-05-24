from time import sleep


def contador(inicio, fim, passos):
    if passos < 0:
        passos *= -1
    if passos == 0:
        passos += 1
    print('_' * 30)
    print(f'Contagem de {inicio} a {fim} de {passos} em {passos}')
    print('_' * 30)
    sleep(0.3)

    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(f'{contador} ', end='')
            sleep(0.3)
            contador += passos
        print('Acabou')
    else:
        contador = inicio
        while contador >= fim:
            print(f'{contador} ', end='')
            sleep(0.4)
            contador -= passos
        print('Acabou')


contador(1, 10, 1)
contador(10, 0, 2)
print('Faça Uma Contagem Personalizada.')
inicio = int(input('Digite Onde Deve Começar: '))
fim = int(input('Digite Onde Deve Terminar: '))
passos = int(input('Qual Deve ser o Passo? '))
contador(inicio, fim, passos)
