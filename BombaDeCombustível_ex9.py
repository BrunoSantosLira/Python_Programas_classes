from time import sleep

class BombaDeCombustível:
    #A
    def __init__(self, TipoCombustível, VLitro, QTADeCombustível):
        self.TipoCombustível= TipoCombustível
        self.VLitro= VLitro
        self.QTADeCombustível= QTADeCombustível
        
    #B
    def abastecerPorLitro(self):
        abastecimento= int(input('Quantos litros deseja abastecer? '))
        print('-'*12)
        print(f'Abastecimento feito com sucesso! \n Valor da conta: R${abastecimento * self.VLitro}')
        self.QTADeCombustível -= abastecimento
        
        
        
    def abastecerPorValor(self):
        abastecimento= int(input('Que valor deseja abastecer? R$'))
        print('-'*12)
        LitrosAbastecidos= abastecimento / self.VLitro
        print(f'Abastecimento feito com sucesso! \n Foram abastecidos {LitrosAbastecidos:.2f} litros')
        self.QTADeCombustível -= LitrosAbastecidos
        
        
    def alterarValor(self):
        self.VLitro= float(input('Para Qual valor deseja alterar o litro? R$'))
        
    def alterarCombustível(self):
        self.TipoCombustível= str(input('Para que tipo de combustível deseja alterar?'))
        
    def alterarQtacombustível(self):
        self.QTADeCombustível= float(input('Que Quantidade de combustível deseja colocar na bomba?'))
        
        
        
bomba1=BombaDeCombustível('Gasolina', 6.00, 1000)
opção=0
while opção != 6:
    print('-='*15)
    print(f'{"Bomba 1"}'.center(30))
    print('-='*15)
    print('1 - Abastecer por Litro')
    print('2 - Abastecer por Valor')
    print('3 - Alterar Valor do combustível')
    print('4 - Alterar tipo de combustível')
    print('5 - Alterar a Quantidade de combustível')
    print('6 - Sair')
    print(f'Quantidade de combustível atual: {bomba1.QTADeCombustível:.2f}')
    opção= int(input('Sua escolha:'))
    
    if opção == 1:
        bomba1.abastecerPorLitro()
        sleep(1)
        
    if opção == 2:
        bomba1.abastecerPorValor()
        sleep(1)
        
    if opção == 3:
        bomba1.alterarValor()
        sleep(1)
        
    if opção == 4:
        bomba1.alterarCombustível()
        sleep(1)
        
    if opção == 5:
        bomba1.alterarQtacombustível()
        sleep(1)
        
    if opção == 6:
        print('Programa Finalizado!')
        sleep(1)
        break