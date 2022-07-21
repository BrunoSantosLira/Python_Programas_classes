class ContaInvestimento:
    #A
    def __init__(self, número_conta, nome_correntista, saldo=1000, taxa_juros=10):
        self.número_conta= número_conta
        self.nome_correntista= nome_correntista
        self.saldo = saldo 
        self.taxa_juros= taxa_juros
     
    #B   
    def alterarNome(self):
        self.nome_correntista= input('Digite o novo nome do correntista:')
        
    def depositar(self):
        while True:
            depósito= int(input('Que valor deseja depositar? R$'))
            if depósito < 0:
                print('Por Favor, não coloque números negativos!')
            else:
                self.saldo += depósito
                print('Valor depositado com sucesso!')
                break
            
    def saque(self):
        while True:
            saque= int(input('Que valor deseja sacar? R$'))
            if self.saldo < 0:
                print('Saque inválido!!! Valor menor que conta com saldo R$0 ou negativo')
            elif self.saldo < saque:
                print('Saque inválido!!! Valor menor que conta com saldo R$0 ou negativo')
            else:
                self.saldo -= saque
                print('Valor sacado com sucesso!')
                break
    
    def AdicioneJuros(self):
        self.saldo= (100 +int(input('De quanto é a taxa que deseja adicionar?'))) * (self.saldo / 100)
        
pessoa1= ContaInvestimento(1,'marcelo')
pessoa1.AdicioneJuros()
print(pessoa1.saldo)

        