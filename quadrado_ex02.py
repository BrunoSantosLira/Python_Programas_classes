class Quadrado:
    #A
    def __init__(self, lado):
        self.lado= lado
    #B    
    def MudarValorLado(self):
        self.lado= int(input('Qual o lado do quadrado?'))   
        
    def RetornarValorLado(self):
        print(f' O valor do lado é {self.lado}')
        
    def CalcularArea(self):
        Área= self.lado * self.lado
        print(f' A área é {Área}')
       
Quadrado1= Quadrado(5)     
Quadrado1.RetornarValorLado()   
Quadrado1.CalcularArea()
Quadrado1.MudarValorLado()
Quadrado1.RetornarValorLado()
Quadrado1.CalcularArea()