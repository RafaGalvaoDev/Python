from datetime import date


def voto():
    idade = date.today().year - ano_Nascimento
    if idade >= 18 and idade <= 70:
        return print(f'Na Sua Idade: {idade} Anos é Obrigatorio Votar.')
    elif idade < 18:
        print(f'Na Sua Idade: {idade} Anos, Não Votar ')
    else:
        print(f'Na Sua Idade: {idade} Anos, O Voto é Opcional')


ano_Nascimento = int(input('Digite em que ano você nasceu: '))
voto()
