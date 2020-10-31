def bubbleSort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if(lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    return lista

lista = [7, 2, 1, 5]
print(bubbleSort(lista))