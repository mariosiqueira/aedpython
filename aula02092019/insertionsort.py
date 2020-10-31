import random

def insertionSort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1
        while (j >= 0 and vetor[j] >= chave):
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    return vetor

vetor = list(range(0, 10))
random.shuffle(vetor)
print('---Vetor desordenado:')
print(vetor)
print('---Vetor ordenado:')
print(insertionSort(vetor))