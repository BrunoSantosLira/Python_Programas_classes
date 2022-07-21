from time import sleep
import os

class Tamagushi:
    #A
    def __init__(self, nome, fome, saude, idade,tédio=0):
        self.nome= nome
        self.fome= fome
        self.saude= saude
        self.idade= idade
        self.tédio= tédio
        
    #B   
    def Info(self):
        print('Niveis de:')
        print('Nome....: ' + str(self.nome))
        print('Fome....: ' + str(self.fome))
        print('Saúde...: ' + str(self.saude))
        print('Idade...: ' + str(self.idade))
        print('Tédio...: ' + str(self.tédio))
        print('Humor...:')
        if self.fome > 80 and self.saude < 30:
            print('Triste')
        if self.fome >=90 and self.saude < 15:
            print('Muito Triste')
        if self.fome <=40 and self.saude >=60:
            print('Feliz')
        if self.fome <=20 and self.saude >=80:
            print('Muito Feliz')
        else:
            print('Razoável')
        
    def AlterarNome(self):
        self.nome= str(input('Digite o novo nome do seu Tamagushi:'))
        
    def AlterarFome(self):
        self.fome= int(input('Digite o nível de fome do seu Tamagushi:'))
        
    def AlterarSaúde(self):
        self.saude= int(input('Digite o nível de saúde do seu Tamagushi:'))
        
    def AlterarIdade(self):
        self.idade= int(input('Digite a idade do seu Tamagushi:'))
        
    #Métodos do ex15
    
    def alimentar(self):
        quantia= int(input('Quanto de comida você quer dar?'))
        self.fome -= quantia
        print(f'A fome do seu bichinho Tamagushi diminuiu')
        self.tédio += 15
        print(f' O tédio do seu tamagushi aumentou!')
        
    def brincar(self):
        minutos= int(input('Ebaaaaa!!! Por quanto tempo vamos brincar???'))
        print('Brincando...')
        sleep(6)
        self.tédio -= minutos

opção=0
bichinho1= Tamagushi('Fernandinho',20,100,1)
while opção != 7:
    os.system('cls')
    print('1 - Alimentar')
    print('2 - Brincar')
    print('3 - Alterar nome')
    print('4 - Alterar fome')
    print('5 - Alterar saúde')
    print('6 - Alterar idade')
    print('7 - Sair')
    opção= int(input('Digite sua opção:'))
    
    if opção == 1 :
        bichinho1.alimentar()
        os.system('pause')
        
    elif opção == 2 :
        bichinho1.brincar()
        os.system('pause')
        
    elif opção == 3 :
        bichinho1.AlterarNome
        os.system('pause')
    
    elif opção == 4 :
        bichinho1.AlterarFome()
        os.system('pause')
        
    elif opção == 5 :
        bichinho1.AlterarSaúde()
        os.system('pause')
        
    elif opção == 6 :
        bichinho1.AlterarIdade()
        os.system('pause')
        
    elif opção == 7 :
        print('Programa Finalizado')
        break
    else:
        os.system('cls')
        print('??????')
        sleep(5)
        print('você entrou no menu secreto!')
        bichinho1.Info()
        
        sleep(5)
        os.system('pause')
        os.system('cls')