import random

def insertion(vetor):
    i = 1
    while (i < len(vetor)):
        temp = vetor[i]
        j = i - 1
        while(j >= 0 and vetor[j] > temp):
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = temp
        i += 1
    return vetor

vetor = list(range(0, 21))
random.shuffle(vetor)
print(insertion(vetor))