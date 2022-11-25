import time, random

listaImpressao = ['prova', 'imagem', 'documento']
parada = 0

print(f'Fila de impressão: {listaImpressao}')

while parada != 1:
    l = len(listaImpressao)

    for x in range(l):

        print("imprimindo arquivo: ", listaImpressao[0])
        t = random.uniform(1, 6)
        time.sleep(t)
        listaImpressao.pop(0)
        print(f'Fila de impressão: {listaImpressao}')
    else:
        print('Não a arquivos na fila')

    parada = int(input('Se quiser sair digite 1: '))
    print(' ================ ')




