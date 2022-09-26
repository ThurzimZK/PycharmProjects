n = int(input('Digite um numero de 1 a 10: '))
if n > 1 and n < 10:
    for tabuada in range(0, 11):
         print(f'{n} X {tabuada} = {n * tabuada}')

