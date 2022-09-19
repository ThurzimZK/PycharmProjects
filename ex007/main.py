num = float(input('Uma distância em metros: '))
k = num / 1000
h = num / 100
da = num / 10
dm = num * 10
c = num * 100
mm = num * 1000
print(f'A medida de {num}m corresponde a \n{k}km\n{h}hm\n{da}dam')
print('{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(dm, c, mm))