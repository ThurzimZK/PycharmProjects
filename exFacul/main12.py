n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 != n2 and n1 != n3:
    if n1 > n2 and n1 > n3 and n2 > n3:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n1,n2,n3))
        input()
    elif n1 > n2 and n1 > n3 and n3 > n2:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n1, n3, n2))
        input()
    elif n2 > n1 and n2 > n3 and n1 > n3:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n2, n1, n3))
        input()
    elif n2 > n1 and n2 > n3 and n3 > n1:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n2, n3, n1))
        input()
    elif n3 > n1 and n3 > n2 and n1 > n2:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n3, n1, n2))
        input()
    elif n3 > n1 and n3 > n2 and n2 > n1:
        print('O maior numero é o {} seguido do {} e por ultimo {}'.format(n3, n2, n1))
        input()
else:
    print('Digite numeros diferentes')
    input()