class Macaco:
    #A
    def __init__(self,nome, bucho=[]):
        self.nome= nome
        self.bucho= bucho=[]
     
     #B
    def comer(self):
        try:
            self.bucho.append(input(f'O que o macaco {self.nome} vai comer?'))
        except:
            self.bucho=[]
            return
     
    def VerBucho(self):
        try:
            print(f'O macaco {self.nome} tem dentro do bucho:')
            for alimento in self.bucho:
                print(alimento)
        except:
            self.bucho=[]
            return
            
    def digerir(self):
         del self.bucho
         print('Todos os alimentos já foram digeridos!')
        
        
#Programa Principal
macaco1= Macaco('Caio')
macaco2= Macaco('Cafeína')
macaco1.comer()
macaco1.VerBucho()

macaco1.comer()
macaco1.VerBucho()

macaco1.comer()
macaco1.VerBucho()
print('-----------')
macaco2.comer()
macaco2.VerBucho()

macaco2.comer()
macaco2.VerBucho()

macaco2.comer()
macaco2.VerBucho()

print(f'No fim o macaco 1 comeu {macaco1.bucho}')
print(f' e o macaco 2 comeu {macaco2.bucho}')


