from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('O ângulo de {} tem TÂNGENTE de {:.2f}'.format(angulo, tan))