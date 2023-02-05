import math
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
hypo = math.hypot(co, ca)
print('A medida do cateto oposto foi {}'.format(co))
print('A medida do cateto adjacente foi {}'.format(ca))
print('A medida da hipotenusa é {:.2f}'.format(hypo))
