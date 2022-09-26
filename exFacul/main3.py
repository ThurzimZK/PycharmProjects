peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite a sua altura em M: '))
imc = peso / (altura * altura)
sexo = str(input('Qual seu sexo [M ou F]? '))

if sexo == 'F':
    if imc < 18:
        print('Abaixo do peso')
    elif imc > 18 and imc < 24:
        print('Peso normal')
    elif imc > 25 and imc < 30:
        print('Sobrepeso')
    elif imc > 30 and imc < 35:
        print('Obesidade moderada')
    elif imc > 35 and imc < 40:
        print('Obesidade grave')
    elif imc > 40:
        print('Obesidade gravíssima')
elif sexo == 'M':
    if imc < 18:
        print('Abaixo do peso')
    elif imc > 18 and imc < 25:
        print('Peso normal')
    elif imc > 25 and imc < 30:
        print('Sobrepeso')
    elif imc > 30 and imc < 35:
        print('Obesidade moderada')
    elif imc > 35 and imc < 40:
        print('Obesidade grave')
    elif imc > 40:
        print('Obesidade gravíssima')