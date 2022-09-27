n = s = 0
vezes = 0
while n !=999:
    n = int(input('Digite um numero: '))
    s += n
    print(s)
    vezes = vezes + 1
    if s >= 80:
        break
print('Foram somados {} valores'.format(vezes))