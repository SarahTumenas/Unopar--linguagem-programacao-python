lista = [10, 4, 1, 15, -3]

lista_ordenada1 = sorted(lista)

lista_ordenada2 = lista.sort()

print('lista = ', lista, '\n')

print('lista_ordenada1 = ', lista_ordenada1)

print('lista_ordenada2 = ', lista_ordenada2)

print('lista = ', lista)

###################################
lista = [7, 4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)

##########################################
lista = [5, -1]

if lista[0] > lista[1]:
    lista[0], lista[1] = lista[1], lista[0]

print(lista)


###########################################
def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista


lista = [10, 9, 5, 8, 11, -1, 3]
executar_selection_sort(lista)
print(lista)


###########################################

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista = [10, 9, 5, 8, 11, -1, 3]
executar_bubble_sort(lista)
print(lista)


###########################################

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        valor_inserir = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
        j -= 1
        lista[j + 1] = valor_inserir
        return lista


lista = [10, 9, 5, 8, 11, -1, 3]
executar_insertion_sort(lista)
print(lista)


###########################################

def executar_merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        esquerda = executar_merge_sort(lista[:meio])
        direita = executar_merge_sort(lista[meio:])
    return executar_merge(esquerda, direita)


def executar_merge(esquerda, direita):
    sub_lista_ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] <= direita[topo_direita]:
            sub_lista_ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        else:
            sub_lista_ordenada.append(direita[topo_direita])
            topo_direita += 1
            sub_lista_ordenada += esquerda[topo_esquerda:]
            sub_lista_ordenada += direita[topo_direita:]
        return sub_lista_ordenada


lista = [15, 9, 5, 8, 11, -1, 3]
executar_merge_sort(lista)
print(lista)


###########################################
def executar_quicksort(lista, inicio, fim):
    if inicio < fim:
        pivo = executar_particao(lista, inicio, fim)
        executar_quicksort(lista, inicio, pivo - 1)
        executar_quicksort(lista, pivo + 1, fim)
    return lista


def executar_particao(lista, inicio, fim):
    pivo = lista[fim]
    esquerda = inicio
    for direita in range(inicio, fim):
        if lista[direita] <= pivo:
            lista[direita], lista[esquerda] = lista[esquerda], lista[direita]
            esquerda += 1
            lista[esquerda], lista[fim] = lista[fim], lista[esquerda]
            return esquerda


lista = [17, 9, 5, 8, 11, -1, 3]
executar_quicksort(lista, inicio=0, fim=len(lista) - 1)
print(lista)
