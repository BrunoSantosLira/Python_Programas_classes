from time import sleep

class carro:
    def __init__(self, consumo, Ncombustível=0):
        self.consumo= consumo
        self.Ncombustível= Ncombustível
        
    def adicionarGasolina(self):
        self.Ncombustível += int(input('Quanto de combustível deseja abastecer?'))
        
    def andar(self):
        caminho = int(input('Quantos KMs você quer andar?'))
        sleep(1)
        print('Dirigindo...')
        sleep(3)
        print('Dirigindo...')    
        gasto= caminho / self.consumo
        if gasto > self.Ncombustível:
            print('A gasolina acabou...')
            self.Ncombustível = 0
        else:
            self.Ncombustível -= gasto
        
    def ObterGasolina(self):
        print(f'Restaram {self.Ncombustível:.2f} Litros de combustível')
        
carro1= carro(15)
print(carro1.Ncombustível)
carro1.adicionarGasolina()
print(carro1.Ncombustível)
print('----------------')
carro1.andar()
carro1.ObterGasolina()