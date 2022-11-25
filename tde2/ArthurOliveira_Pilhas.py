lista = []
quociente = 1

numDigitado = int(input('Digite um numero decimal: '))
dividendo = numDigitado

while quociente >= 1:
    resto = dividendo % 2
    lista.insert(0, resto)
    quociente = dividendo // 2
    dividendo = quociente

binario = ''.join(map(str, lista))
print(f'O numero digitado em binario é: {binario}')
