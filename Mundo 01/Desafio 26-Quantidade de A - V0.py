from emoji import emojize
es = emojize(':writing_hand:')
sy = emojize(':input_symbols:')
le = emojize(':input_latin_letters:')
cor0 = '\033[m'
cor1 = '\033[0;30;42m'
cor2 = '\033[0;30;44m'
cor3 = '\033[0;30;45m'
cor4 = '\033[0;30;41m'
frase = str(input('{}Digite{} uma frase:{} '.format(cor1, es, cor0))).strip()
fm = frase.lower()
pa = fm.index('a')
ua = fm.rfind('a')
qa = fm.count('a')
print('A letra{} {}A aparece primeiro na possição {}{}'.format(sy, cor3, pa+1, cor0))
print('A letra{} {}A aparece{} {} vezes '.format(le, cor2, cor0, qa))
print('A letra{} A aparece por último na possição {} {}'.format(cor4, ua+1, cor0))

