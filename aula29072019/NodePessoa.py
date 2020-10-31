class NodePessoa:
    def __init__(self, identificacao, nome, cpf):
        self.identificacao = identificacao
        self.nome = nome
        self.cpf = cpf
        self.proximo = None
    
    def toString(self):
        return 'Identificacao: ' + str(self.identificacao) + ' Nome: ' + self.nome + ' CPF: ' + self.cpf