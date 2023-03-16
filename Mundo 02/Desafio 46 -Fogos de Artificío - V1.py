from time import sleep
for contagem in range(10, 0-1, -1):
    print('Faltam {:2} segundo '.format(contagem, sleep(1)))
    if contagem == 0:
        print('Olha os fogos de artifício, que lindos')
