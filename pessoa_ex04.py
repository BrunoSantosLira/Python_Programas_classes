from random import randint,uniform


class Pessoa:
    #A
    def __init__(self, nome, idade, peso, altura):
        self.nome= nome
        self.idade= idade
        self.peso= peso
        self.altura= altura
    #B    
    def engordar(self):
        ganho= randint(1,5)
        self.peso += ganho
        print(f'Engordei {ganho}kg')
        
    def emagrecer(self):
        perda= randint(1,5)
        self.peso -= perda
        print(f'emagreci {perda}kg')
        
    def crescer(self):
        crescimento= uniform(0.01,0.05)
        self.altura += crescimento
        print(f'Cresci {crescimento:.2f}cm!')
        
    def envelhecer(self):
        Anos= randint(1,5)
        for c in range(Anos):
            self.idade += 1
            if self.idade < 21:
             self.altura += 0.05
        print(f'Envelheci {Anos} anos, como o tempo passa...')
        
        
        
pessoa1= Pessoa('gustavo',18,49.8, 1.79)
pessoa1.engordar()
print(pessoa1.peso)
pessoa1.emagrecer()
print(pessoa1.peso)
print('------------')
pessoa1.crescer()
print(f'{pessoa1.altura:.2f}')
print('----------')
pessoa1.envelhecer()
print(pessoa1.idade)
print(f'{pessoa1.altura:.2f}')