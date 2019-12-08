# classe pai, herança
from Pessoa import Pessoa

# instanciação
class Aluno(Pessoa):        
    def __init__(self):
        pass

      # Metodo serMatricula para inserir
    def setMatricula(self,matricula):
        self._matricula = matricula
        
    # Metodo getMatricula para retornar 
        return self._matricula
    
  