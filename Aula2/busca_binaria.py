import lista as lista


def executar_busca_binaria(lista, valor):

    minimo = 0

    maximo = len(lista) - 1

    while minimo <= maximo:
     meio = (minimo + maximo) // 2 #Encontra o elemento que divide a lista ao meio
# Verifica se o valor procurado está a esquerda ou direitado valor central
    if valor < lista[meio]:
        maximo = meio - 1
    elif valor > lista[meio]:
           minimo = meio + 1
    else:
        return True
    return False