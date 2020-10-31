import random

def gnomeSort(vetor):
    pivot = 0
    while (pivot < len(vetor) - 1):
        if(vetor[pivot] > vetor[pivot + 1]):
            menor = vetor[pivot + 1]
            vetor[pivot + 1] = vetor[pivot]
            vetor[pivot] = menor
            if(pivot > 0):
                pivot -= 2
        pivot += 1
    return vetor

vetor = list(range(0, 10))
random.shuffle(vetor)
print(vetor)
print(gnomeSort(vetor))
