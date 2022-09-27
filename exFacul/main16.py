n = int(input('Digite um numero: '))
n2 = int(input('Digite a potencia: '))
if n > 0 and n2 > 0:
    x = n ** n2
    print('O resultado é {}'.format(x))
else:
    print('Este numero não é valido, digite um numero positivo')
