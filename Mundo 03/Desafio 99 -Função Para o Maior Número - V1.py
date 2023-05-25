from time import sleep


def maior(* numero):
    total = maix = 0
    print('_' * 35)
    for index, valor in enumerate(numero):
        print(f'{valor}: ', end='')
        total += 1
        sleep(0.5)
        for valor in numero:
            if maix < valor:
                maix = valor
    print(f'Foi Informado {total} Números')
    sleep(0.5)
    print(f'{maix} Foi o Maior Número')
    sleep(0.5)
    print('_' * 35)
    sleep(0.5)


maior(1, 2, 3, 0)
maior(0, 6)
maior(9, 0, 3, 5, 1)
maior(10, 23, 34, 1, 9)
maior()
