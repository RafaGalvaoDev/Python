def factorial(numero=1, ):
    facto = 1
    for contador in range(numero, 0, -1):
        print(f'Fatorial de {numero} X {contador} é igual a {facto} ')
        facto *= contador
    return facto


factorial(10)
