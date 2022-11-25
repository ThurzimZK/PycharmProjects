palavra = str(input('Digite uma palavra: '))

contrario = ''.join(reversed(palavra))

if contrario == palavra:
    print('É um palindromo')
else:
    print('Não é um palindromo')
