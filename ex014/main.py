dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
valor = (dia * 60) + (km * 0.15)
print('O valor a pagar é de R${:.2f}'.format(valor))