def notas(*numeros, situacao=False):
    """
    O Programa Calcula a Média, O Maior Valor Informado, O Menor Valor Informado e O Total de Valores Informados
    :param numeros: Pegar as Notas
    :param situacao: Mostra a Situação da Turma
    :return: Mostra o Dicionario
    """
    lista = dict()
    lista['Total'] = len(numeros)
    lista['Maior'] = max(numeros)
    lista['Menor'] = min(numeros)
    lista['Media'] = sum(numeros)/len(numeros)
    if situacao:
        if lista['Media'] > 7:
            lista['situacao'] = 'Boa'
        elif lista['Media'] >= 5:
            lista['situacao'] = 'Pode Melhorar'
        else:
            lista['situacao'] = 'Ruim'
    return lista


resposta = notas(5.2, 6, 8.4, 10, 9, situacao=True)
print(resposta)
