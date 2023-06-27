def leiadinheiro(mensagem):
    sim = False
    while not sim:
        entrada = str(input(mensagem)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('Tente Outra Vez ')
        else:
            sim = True
            return float(entrada)
