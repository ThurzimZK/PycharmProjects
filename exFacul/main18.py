n = int(input('Quantas notas voce quer somar: '))
s = 0
i = 0
while i < n:
    nota = int(input('Digite sua nota: '))
    s += nota
    i = i + 1
media = s / n
print(media)

