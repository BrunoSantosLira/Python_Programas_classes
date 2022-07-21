from time import sleep

class Retângulo:
    #A
    def __init__(self, Comprimento, largura):
        self.Comprimento = Comprimento
        self.largura = largura
        
    #B
    def MudarValorDosLados(self):
        self.Comprimento= int(input('Digite uma nova Comprimento:'))
        self.largura= int(input('Digite uma nova largura:'))
    
    
    def RetornarValorDosLados(self):
        print(f'Comprimento....= {self.Comprimento}')
        print(f'largura .= {self.largura}')
    
    def CalcularÁrea(self):
        Área= self.Comprimento * self.largura
        return Área
        
    def CalcularPerímetro(self):
        Perímetro = (self.Comprimento + self.Comprimento) + (self.largura + self.largura)
        return Perímetro
 
#C        
print('-'*40)
print(f'{"Calculador de pisos e rodapés"}'.center(40))
print('-'*40)
comp=int(input('Digite o comprimento:'))
larg=int(input('Digite a largura:'))
Figura= Retângulo(comp,larg)
print('Calculando...')
sleep(1.5)
print(f'Com essas medidas que você me deu, teriamos que ter:')
print(f'{Figura.CalcularÁrea()} pisos')
print(f'{Figura.CalcularPerímetro()} rodapés')