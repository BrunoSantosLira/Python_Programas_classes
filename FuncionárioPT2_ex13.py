class Funcionário:
    def __init__(self, nome, salário):
        self.nome= nome
        self.salário= salário
         
    @property
    def salário(self):
        return self._salário
    
    @salário.setter
    def salário(self,valor):
        if isinstance(valor, str):
            valor= float(valor.replace('R$',' '))    
        self._salário= valor
        
    def Voltar_salário(self):
        print(f'Salário: R${self.salário}')
        
    def Voltar_nome(self):
        print(f'Nome: {self.nome}')
        
    def aumentarSalário(self):
        aumento= float(input('Em quantos % o salário deve ser aumentado? '))
        self.salário = (100 + aumento) * (self.salário / 100)

        
        
funcionario1= Funcionário('Roberto','R$100')
funcionario1.aumentarSalário()
funcionario1.Voltar_salário()
funcionario1.Voltar_nome()