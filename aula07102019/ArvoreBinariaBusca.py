from aula07102019.No import No

class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None
    
    def inserir(self, chave, noAtual):
        novoNo = No(chave)
        if(self.estaVazio()):
            self.raiz = novoNo
        else:
            if(chave <= noAtual.chave):
                if(noAtual.esquerdo != None):
                    self.inserir(chave, noAtual.esquerdo)
                else:
                    novoNo.pai = noAtual
                    noAtual.esquerdo = novoNo
            else:
                if(noAtual.direito != None):
                    self.inserir(chave, noAtual.direito)
                else:
                    novoNo.pai = noAtual
                    noAtual.direito = novoNo
    
    def remover(self, chave):
        noEscolhido = self.buscar(chave, self.raiz)

    def buscar(self, chave, noAtual):
        if(noAtual != None):
            if(chave < noAtual.chave):
                return self.buscar(chave, noAtual.esquerdo)
            elif(chave > noAtual.chave):
                return self.buscar(chave, noAtual.direito)
            else:
                return noAtual
        else:
            print('passei aqui')
            return None
  
    def maximo(self, noAtual):
        if(noAtual.direito != None):
            return self.maximo(noAtual.direito)
        else:
            return noAtual
  
    def minimo(self, noAtual):
        if(noAtual.esquerdo != None):
            return self.minimo(noAtual.esquerdo)
        else:
            return noAtual
  
    def sucessor(self, chave):
        if((self.buscar(chave, self.raiz).direito) != None):
            return self.minimo((self.buscar(chave, self.raiz)).direito)
        else:
            return None

    def predecessor(self, chave):
        if((self.buscar(chave, self.raiz).esquerdo) != None):
            return self.maximo((self.buscar(chave, self.raiz)).esquerdo)
        else:
            return None
       
    def estaVazio(self):
        if(self.raiz == None):
            return True
        else:
            return False

    def imprimir(self, ordem, noAtual):
        if(ordem.lower() == 'pre' and noAtual != None):
            print(noAtual.chave, end=' ')
            self.imprimir(ordem, noAtual.esquerdo)
            self.imprimir(ordem, noAtual.direito)
    
        elif(ordem.lower() == 'ord' and noAtual != None):
            self.imprimir(ordem, noAtual.esquerdo)
            print(noAtual.chave, end=' ')
            self.imprimir(ordem, noAtual.direito)
    
        elif(ordem.lower() == 'pos' and noAtual != None):
            self.imprimir(ordem, noAtual.esquerdo)
            self.imprimir(ordem, noAtual.direito)
            print(noAtual.chave, end=' ')
