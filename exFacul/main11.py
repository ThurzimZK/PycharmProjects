salario = float(input('Qual seu salario? R$'))
if salario > 0:
    if salario < 1200:
        print('Seu salario nao tem desconto')
    elif salario > 1200 and salario < 3500:
        desconto = salario * 0.094
        valorF = salario - desconto
        print('Com os descontos seu salario ficu R${}'.format(valorF))
    elif salario > 3500:
        desconto = salario *0.211
        valorF = salario - desconto
        print('Com os descontos seu salario ficu R${}'.format(valorF))