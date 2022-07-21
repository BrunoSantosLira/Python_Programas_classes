
class Bola:
    #A
    def __init__(self, cor, circunferência, material):
        self.cor = cor
        self.circunferência = circunferência
        self.material = material
    #
    def MostrarCor(self):
        print(self.cor)
        
    def TrocarCor(self):
        self.cor=input('Para que cor deseja trocar?')


bola1= Bola('Amarela','5','Borracha')
bola1.MostrarCor()
bola1.TrocarCor()
bola1.MostrarCor()