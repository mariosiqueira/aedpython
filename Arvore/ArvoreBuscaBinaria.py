from No import No

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, chave, noAtual):
        novoNo = No(chave)
        if(self.raiz == None):
            self.raiz = novoNo
        else:
            if(novoNo.chave <= noAtual.chave):
                if(noAtual.esquerdo == None):
                    novoNo.pai = noAtual
                    noAtual.esquerdo = novoNo
                else:
                    self.inserir(chave, noAtual.esquerdo)
            
            else:
                if(noAtual.direito == None):
                    novoNo.pai = noAtual
                    noAtual.direito = novoNo
                else:
                    self.inserir(chave, noAtual.direito)
    
    def remover(self, chave, noAtual):
        noEscolhido = self.buscar(chave, self.raiz)
        if(noEscolhido == None):
            return False
        else:
            #Remocao no Folha
            if(noEscolhido.esquerdo == None and noEscolhido.direito == None):
                if(noEscolhido.pai != None):
                    if(noEscolhido.pai.esquerdo == noEscolhido):
                        noEscolhido.pai.esquerdo = None
                        noEscolhido.pai = None
                        noEscolhido = None
                    elif(noEscolhido.pai.direito == noEscolhido):
                        noEscolhido.pai.direito = None
                        noEscolhido.pai = None
                        noEscolhido = None
                else: #noEscolhido = raiz da arvore
                    self.raiz = None
                return True
            
            #Remocao de no com um filho
            elif((noEscolhido.esquerdo != None and noEscolhido.direito == None) or (noEscolhido.esquerdo == None and noEscolhido.direito != None)):
                if(noEscolhido.pai.esquerdo == noEscolhido):
                    if(noEscolhido.esquerdo != None):
                        noEscolhido.esquerdo.pai = noEscolhido.pai
                        noEscolhido.pai.esquerdo = noEscolhido.esquerdo
                        noEscolhido.pai = None
                        noEscolhido.esquerdo = None
                        noEscolhido = None
                    else:
                        print('passei aqui')
                        noEscolhido.direito.pai = noEscolhido.pai
                        noEscolhido.pai.esquerdo = noEscolhido.direito
                        noEscolhido.pai = None
                        noEscolhido.direito = None
                        noEscolhido = None
                else:
                    if(noEscolhido.esquerdo != None):
                        noEscolhido.esquerdo.pai = noEscolhido.pai
                        noEscolhido.pai.direito = noEscolhido.esquerdo
                        noEscolhido.pai = None
                        noEscolhido.esquerdo = None
                        noEscolhido = None
                    else:
                        noEscolhido.direito.pai = noEscolhido.pai
                        noEscolhido.pai.direito = noEscolhido.direito
                        noEscolhido.pai = None
                        noEscolhido.direito = None
                        noEscolhido = None
                return True
            
            #Remocao de no com dois filhos
            elif(noEscolhido.esquerdo != None and noEscolhido.direito != None):
                sucessor = self.sucessor(noEscolhido)
                if(noEscolhido.pai == None):
                    #Remoção da raiz
                    if(sucessor.direito != None):
                        sucessor.direito.pai = sucessor.pai
                        sucessor.pai.esquerdo = sucessor.direito
                    sucessor.direito = noEscolhido.direito
                    noEscolhido.direito.pai = sucessor
                    sucessor.esquerdo = noEscolhido.esquerdo
                    noEscolhido.esquerdo.pai = sucessor
                    noEscolhido = None
                else:
                    if(sucessor.direito != None):
                        #Sucessor tem filho
                        sucessor.direito.pai = sucessor.pai.esquerdo
                        sucessor.pai.esquerdo = sucessor.direito
                    if(noEscolhido.esquerdo != None):
                        sucessor.esquerdo = noEscolhido.esquerdo
                        noEscolhido.esquerdo.pai = sucessor
                    noEscolhido.direito.pai = sucessor
                    sucessor.direito = noEscolhido.direito
                    if(noEscolhido.pai.esquerdo == None):
                        #noEscolhido é o filho da direita
                        sucessor.pai = noEscolhido.pai
                        noEscolhido.pai.direito = sucessor
                        noEscolhido = None
                    else:
                        #noEscolhido é o filho da esquerda
                        sucessor.pai = noEscolhido.pai
                        noEscolhido.pai.esquerdo = sucessor
                        noEscolhido = None
                    
    def buscar(self, chave, noAtual):
        if(chave < noAtual.chave):
            if(noAtual.esquerdo != None):
                return self.buscar(chave, noAtual.esquerdo)
            else:
                return None
            
        elif(chave > noAtual.chave):
            if(noAtual.direito != None):
                return self.buscar(chave, noAtual.direito)
            else:
                return None
            
        else:
            return noAtual
      
    def estaVazio(self):
        if(self.raiz == None):
            return True
        else:
            return False
        
    def imprimir(self, ordem, noAtual):
        if(ordem.lower() == 'pre' and noAtual != None):
            print(noAtual.chave, end = ' ')
            self.imprimir(ordem, noAtual.esquerdo)
            self.imprimir(ordem, noAtual.direito)
            
        elif(ordem.lower() == 'ord' and noAtual != None):
            self.imprimir(ordem, noAtual.esquerdo)
            print(noAtual.chave, end = ' ')
            self.imprimir(ordem, noAtual.direito)
        
        elif(ordem.lower() == 'pos' and noAtual != None):
            self.imprimir(ordem, noAtual.esquerdo)
            self.imprimir(ordem, noAtual.direito)
            print(noAtual.chave, end = ' ')
        
        else:
            return None
    
    def minimo(self, noAtual):
        if(noAtual.esquerdo != None):
            return self.minimo(noAtual.esquerdo)
        else:
            return noAtual
    
    def maximo(self, noAtual):
        if(noAtual.direito != None):
            return self.maximo(noAtual.direito)
        else:
            return noAtual
    
    def sucessor(self, noAtual):
        if(noAtual.direito != None):
            return self.minimo(noAtual.direito)
    
    def predecessor(self, noAtual):
        if(noAtual.esquerdo != None):
            return self.maximo(noAtual.esquerdo)
    