n = int(input('Digite um numero: '))
if n > 0:
    if (n % 2 == 0):
        print('Este numero é par!')
    elif (n % 2 == 1):
        print('Este numero é impar!')
else:
    print('Este numero nao é valido')