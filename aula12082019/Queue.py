from aula12082019.NodeQueue import Nodequeue

class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserir(self, elemento):
        novoNode = Nodequeue(elemento)
        if(self.inicio == self.fim == None):
            self.inicio = self.fim = novoNode
            
        else:
            self.fim.proximo = novoNode
            self.fim = novoNode
        self.tamanho += 1
        return True
    
    def remover(self):
        aux = self.inicio
        if(self.inicio == self.fim == None):
            print('Fila Vazia!')
            return None
        elif(self.inicio == self.fim and self.tamanho == 1):
            self.inicio = self.fim = None
        else:
            aux = self.inicio.proximo
            self.inicio.proximo = None
            self.inicio = aux
            self.tamanho -= 1
            return True
    
    def imprimirQueue(self):
        aux = self.inicio
        if(self.tamanho == 0):
            print('Lista Vazia!')
        else:
            while(aux != None):
                print(aux.elemento)
                aux = aux.proximo
            
            
'''
codigo pilha

            while(aux.proximo != self.fim):
                aux = aux.proximo
            aux.proximo = None
            self.fim = aux
            self.tamanho -= 1
            return True  
'''
    
