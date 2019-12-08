#  Classe pai 
class Pessoa:

    # Metodo construtor 
    
    def __init__(self):
        super().__init__()
        pass 


    # SetNome para Inserir 
    def setNome(self,nome):
        self._nome = nome

    # SetSobrenome para Inserir 
    def setSobrenome(self,sobrenome):
        self._sobrenome = sobrenome

    # GetSobrenome para retornar
    def getSobrenome(self):
        return self._sobrenome

    # GetNome para retornar
    def getNome(self):
        return self._nome

