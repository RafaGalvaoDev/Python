frase = str(input('Digite uma frase: ')).strip()
fm = frase.lower()
pa = fm.index('a')
ua = fm.rfind('a')
qa = fm.count('a')
print('A letra A aparece primeiro na possição {}'.format(pa+1))
print('A letra A aparece {} vezes '.format(qa))
print('A letra A aparece por último na possição {}'.format(ua+1))

