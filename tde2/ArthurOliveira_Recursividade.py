def torreHanoi(n, torreAtual, destino, auxiliary):
    if n == 1:
        print("Mova o disco 1 da Torre", torreAtual, "para Torre", destino)
        return
    torreHanoi(n - 1, torreAtual, auxiliary, destino)
    print("Mova o disco", n, "da Torre", torreAtual, "para a Torre", destino)
    torreHanoi(n - 1, auxiliary, destino, torreAtual)

n = 3
torreHanoi(n, '1', '2', '3')
