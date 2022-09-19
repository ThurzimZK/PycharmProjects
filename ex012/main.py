salario = float(input('Qual é o salário do Funcionário? R$'))
valorF = salario + (salario * 0.15)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, valorF))
# input apenas para nao sumir o codigo via cmd
input()