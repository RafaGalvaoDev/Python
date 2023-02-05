import math
ang = float(input('Digite o valor de um angulo qualquer: '))
ra = math.radians(ang)
sen = math.sin(ra)
con = math.cos(ra)
tan = math.tan(ra)
print('O valor digitado foi {} e o seu seno é {:.2f}'.format(ang, sen))
print('O valor digitado foi {} e o seu cosseno é {:.2f}'.format(ang, con))
print('O valor digitado foi {} e a sua tangente é {:.2f}'.format(ang, tan))

