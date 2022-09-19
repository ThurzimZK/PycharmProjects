from math import hypot
catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
hip = hypot(catO, catA)
print('A hipotenusa vai medir {:.2f}'.format(hip))
input()