l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
tinta = area / 2
print('Sua parede tem a dimensão {}x{} e sua área é de {:.1f}m2\nPara pintar essa parede, você precisará de {:.1f}l de tinta.'.format(l, a, area, tinta))
