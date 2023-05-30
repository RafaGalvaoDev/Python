def voto():
    from datetime import date
    idade = date.today().year - ano_Nascimento
    if 70 >= idade >= 18:
        return print(f'Na Sua Idade: {idade} Anos é Obrigatorio Votar.')
    elif idade < 16:
        print(f'Na Sua Idade: {idade} Anos, Não Votar ')
    else:
        print(f'Na Sua Idade: {idade} Anos, O Voto é Opcional')


ano_Nascimento = int(input('Digite em que ano você nasceu: '))
voto()
