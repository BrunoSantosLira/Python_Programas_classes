class ContaCorrente:
    #A
    def __init__(self, número_conta, nome_correntista, saldo=0):
        self.número_conta= número_conta
        self.nome_correntista= nome_correntista
        self.saldo= saldo
     
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


        
        
pessoa1= ContaCorrente(1351,'Marcelo Queiroz')
print(pessoa1.nome_correntista)
pessoa1.alterarNome()
print(f' Novo Correntista da conta: {pessoa1.nome_correntista}')
print('-----------------------------------')
print(F'R${pessoa1.saldo}')
pessoa1.depositar()
print(f'R${pessoa1.saldo}')
print('------------------------')
pessoa1.saque()
print(f'Saldo Restante: R${pessoa1.saldo}')