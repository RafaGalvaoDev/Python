import emoji
num = int(input('Digite um número: '))
x1 = num * 1
x2 = num * 2
x3 = num * 3
x4 = num * 4
x5 = num * 5
x6 = num * 6
x7 = num * 7
x8 = num * 8
x9 = num * 9
x10 = num * 10
xx1 = emoji.emojize(':keycap_1:')
xx2 = emoji.emojize(':keycap_2:')
xx3 = emoji.emojize(':keycap_3:')
xx4 = emoji.emojize(':keycap_4:')
xx5 = emoji.emojize(':keycap_5:')
xx6 = emoji.emojize(':keycap_6:')
xx7 = emoji.emojize(':keycap_7:')
xx8 = emoji.emojize(':keycap_8:')
xx9 = emoji.emojize(':keycap_9:')
xx10 = emoji.emojize(':keycap_10:')
cor0 = '\033[m'
cor1 = '\033[7;32;40m'
print('{}O valor digitado foi {} e sua multiplicação vezes 1{} é {}{}'.format(cor1, num, xx1, x1, cor0))
print('O valor digitado foi {} e sua multiplicação vezes 2{} é {}'.format(num, xx2, x2))
print('{}O valor digitado foi {} e sua multiplicação vezes 3{} é {}{}'.format(cor1, num, xx3, x3, cor0))
print('O valor digitado foi {} e sua multiplicação vezes 4{} é {}'.format(num, xx4, x4))
print('{}O valor digitado foi {} e sua multiplicação vezes 5{} é {}{}'.format(cor1, num, xx5, x5,cor0))
print('O valor digitado foi {} e sua multiplicação vezes 6{} é {}'.format(num, xx6, x6))
print('{}O valor digitado foi {} e sua multiplicação vezes 7{} é {}{}'.format(cor1, num, xx7, x7, cor0))
print('O valor digitado foi {} e sua multiplicaçã vezes 8{} é {}'.format(num, xx8, x8))
print('{}O valor digitado foi {} e sua multiplicação vezes 9{} é {}{}'.format(cor1, num, xx9, x9, cor0))
print('O valor digitado foi {} e sua multiplicação vezes 10{} é {}'.format(num, xx10, x10))
