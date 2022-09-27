x = int(input('Quantas numeros pares voce quer somar: '))
s = 0
i = 0
while i < x:
    n = int(input('Digite um numero par: '))
    if (n % 2 == 0):
        s += n
        i = i + 1
    else:
        print('Esse não é um numero par')
print(s)

