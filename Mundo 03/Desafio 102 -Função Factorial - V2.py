def factorial(numero=1, show=False):
    facto = 1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(f' X ', end='')
            else:
                print(' = ', end='')
        facto *= contador
    return facto


print(factorial(10, show=True))
