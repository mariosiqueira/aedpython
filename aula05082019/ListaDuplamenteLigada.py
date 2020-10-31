from aula05082019.NodeDuplo import NodeDuplo
class ListaDuplamenteLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserirInicio(self, chave):
        novoNode = NodeDuplo(chave)
        if(self.inicio == self.fim == None):
            self.inicio = self.fim = novoNode
            self.tamanho += 1
            return True
        else:
            novoNode.proximo = self.inicio
            self.inicio.anterior = novoNode
            self.inicio = novoNode
            self.tamanho += 1
            return True
    
    def inserirFim(self, chave):
        novoNode = NodeDuplo(chave)
        if(self.inicio == self.fim == None):
            return self.inserirInicio(chave)
        
        else:
            self.fim.proximo = novoNode
            novoNode.anterior = self.fim
            self.fim = novoNode
            self.tamanho += 1
            return True
    
    def inserir(self, chave, indice):
        novoNode = NodeDuplo(chave)
        if(self.inicio == self.fim == None or indice <= 0):
            return self.inserirInicio(chave)
        
        elif(indice >= self.tamanho):
            return self.inserirFim(chave)
        
        else:
            cont = 0
            anterior = atual = self.inicio
            while (cont < indice):
                anterior = atual
                atual = atual.proximo
                cont += 1
            novoNode.anterior = anterior
            novoNode.proximo = atual
            anterior.proximo = novoNode
            atual.anterior = novoNode
            self.tamanho += 1
            return True
    
    def removerInicio(self):
        if(self.inicio == self.fim != None):
            self.inicio = self.fim = None
            self.tamanho -= 1
            return True
        
        elif(self.inicio == self.fim == None):
            print('Lista Vazia!')
            return None
        
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
            self.tamanho -= 1
            return True
    
    def removerFim(self):
        if(self.inicio == self.fim != None):
            return self.removerInicio()
        
        elif(self.inicio == self.fim == None):
            print('Lista Vazia!')
            return None
        
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -= 1
            return True
    
    def remover(self, indice):
        if(indice <= 0):
            return self.removerInicio()
        
        elif(indice >= self.tamanho - 1):
            return self.removerFim()
        
        else:
            anterior = atual = self.inicio
            cont = 0
            while(cont < indice):
                anterior = atual
                atual = atual.proximo
                cont += 1
            anterior.proximo = atual.proximo
            atual.proximo.anterior = anterior
            atual.anterior = None
            atual.proximo = None
            atual = None
            self.tamanho -= 1
            return True
    
    def imprimirLista(self):
        aux = self.inicio
        while (aux != None):
            print(aux.chave)
            aux = aux.proximo
    
    def imprimirListaReversa(self):
        aux = self.fim
        while(aux != None):
            print(aux.chave)
            aux = aux.anterior
    
    def imprimirTamanho(self):
        return self.tamanho