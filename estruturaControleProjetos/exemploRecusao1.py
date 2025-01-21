def imprimir(maximo, atual):
    # condição de parada
    if atual < maximo:
        print(atual)
        imprimir(maximo, atual + 1)
    
    
imprimir(100, 1)
