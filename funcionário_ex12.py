class Funcionário:
    def __init__(self, nome, salário):
        self.nome= nome
        self.salário= salário
        
    def Voltar_salário(self):
        print(f'Salário: R${self.salário}')
        
    def Voltar_nome(self):
        print(f'Nome: {self.nome}')
        
    @property
    def salário(self):
        return self._salário
    
    @salário.setter
    def salário(self,valor):
        if isinstance(valor, str):
            valor= float(valor.replace('R$',' '))    
        self._salário= valor
        
        
funcionario1= Funcionário('Roberto','R$1500')
funcionario1.Voltar_salário()
funcionario1.Voltar_nome()