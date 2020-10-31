from aula29072019.NodePessoa import NodePessoa

class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def inserirInicio(self, identificacao, nome, cpf):
        nodePessoa = NodePessoa(identificacao, nome, cpf)
        if(self.inicio == self.fim == None):
            self.inicio = self.fim = nodePessoa
            self.tamanho += 1
            return True
        else:
            nodePessoa.proximo = self.inicio
            self.inicio = nodePessoa 
            self.tamanho += 1
            return True
    
    def inserirFim(self, identificacao, nome, cpf):
        nodePessoa = NodePessoa(identificacao, nome, cpf)
        if(self.inicio != None and self.fim != None):
            self.fim.proximo = nodePessoa
            self.fim = nodePessoa
            self.fim.proximo = None
            self.tamanho += 1
            return True
        else:
            self.inserirInicio(identificacao, nome, cpf)
            return True
    
    def inserir(self, identificacao, nome, cpf, indice):
        nodePessoa = NodePessoa(identificacao, nome, cpf)
        if((self.inicio == None and self.fim == None) or indice <= 0):
            return self.inserirInicio(identificacao, nome, cpf)
        elif(indice >= self.tamanho):
            return self.inserirFim(identificacao, nome, cpf)
        else:
            atual = self.inicio
            anterior = self.inicio
            contador = 0
            while contador < indice:
                anterior = atual
                atual = atual.proximo
                contador += 1
            anterior.proximo = nodePessoa
            nodePessoa.proximo = atual
            self.tamanho += 1
            return True
    
    def removerInicio(self):
        if(self.tamanho > 0):
            aux = self.inicio
            self.inicio = self.inicio.proximo
            aux.proximo = None
            aux = None
            self.tamanho -= 1
            return True
        else:
            print('Lista Vazia!')
            return None
    
    def removerFim(self):
        if(self.tamanho > 0):
            if(self.inicio == self.fim):
                return self.removerInicio()
            else:
                penultimo = self.inicio
                while penultimo.proximo != self.fim:
                    penultimo = penultimo.proximo
                penultimo.proximo = None
                self.fim = penultimo
                self.tamanho -= 1
                return True
        else:
            print('Lista Vazia!')
            return None
    
    def remover(self, indice):
        if(indice <= 0 and self.tamanho > 0):
            return self.removerInicio()
        
        elif(indice >= self.tamanho - 1 and self.tamanho > 0):
            return self.removerFim()
        
        elif(self.tamanho > 0):   
            anterior = atual = self.inicio
            contador = 0
            while contador < indice:
                anterior = atual
                atual = atual.proximo
                contador += 1
            anterior.proximo = atual.proximo
            atual.proximo = None
            atual = None
            self.tamanho -= 1
            return True
        else:
            print('Lista Vazia!')
            return None
            
    def imprimirLista(self):
        aux = self.inicio
        while(aux != None):
            print('Id: ' + str(aux.identificacao) + ' Nome: ' + aux.nome + ' CPF: ' + aux.cpf)
            aux = aux.proximo
    
    def imprimirTamanho(self):
        return self.tamanho
    
    def buscarElemento(self, indice):
        if(self.tamanho > 0):
            contador = 0
            elemento = self.inicio
            while contador < indice:
                elemento = elemento.proximo
                contador += 1
            return elemento
        else:
            return None