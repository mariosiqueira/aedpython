import random
import time

def bubble(vetor):
    i = 0
    while(i < len(vetor)):
        j = 0
        while(j < len(vetor)):
            if(vetor[i] <= vetor[j]):
                menor = vetor[i]
                vetor[i] = vetor[j]
                vetor[j] = menor
            j += 1
        i += 1
    return vetor

vetor = list(range(0,10000))
random.shuffle(vetor)
print(vetor)
tempoInicial = time.time()
print(bubble(vetor))
tempoFinal = time.time()
print(tempoFinal - tempoInicial)