import random

def gnomeSort(vetor):
    pivot = 0
    while (pivot < len(vetor) - 1):
        if(vetor[pivot] > vetor[pivot + 1]):
            menor = vetor[pivot + 1]
            vetor[pivot + 1] = vetor[pivot]
            vetor[pivot] = menor
            if(pivot > 0):#Verifica se tem elemento antes do pivot
                pivot -= 1 #fez troca e tem anterior, decrementa.
        else:#o pivot e seu proximo estao em ordem.
            pivot += 1 #incrementa o pivot
    return vetor

vetor = list(range(0, 21))
random.shuffle(vetor)
print(gnomeSort(vetor))