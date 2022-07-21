from time import sleep
import os
from random import randint

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
        print('Informações:')
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
        
    
    def alimentar(self):
        self.fome -= quantia
        print(f'A fome do seu bichinho Tamagushi diminuiu')
        self.tédio += 15
        print(f' O tédio do seu tamagushi aumentou!')
    
    
    def brincar(self):
        print('Brincando...')
        sleep(6)
        self.tédio -= minutos
        print('O tédio diminuiu, mas a fome aumentou')
        self.fome  += minutos
        
    def ouvir(self):
        print('Conversando...')
        sleep(1)
        self.tédio -= conversa
        return
    
    
#Programa Principal
opção=0
lista= [Tamagushi('Gustavo',randint(0,100),100,1,randint(0,100)), Tamagushi('Carlinhos',randint(0,100),100,2,randint(0,100))]
while opção != 7:
    os.system('cls')
    print('1 - Alimentar')
    print('2 - Brincar')
    print('3 - Ouvir')
    print('4 - Alterar fome')
    print('5 - Alterar saúde')
    print('6 - Alterar idade')
    print('7 - Alterar nome')
    print('8 - Sair')
    opção = int(input('Digite sua opção:'))
    
    if opção == 1 :
        quantia= int(input('Quanto de alimento você quer dar a eles?'))
        for i,obj in enumerate(lista):
            lista[i].alimentar()
        os.system('pause')
        
    elif opção == 2 :
        minutos= int(input('Ebaaaaa!!! Por quanto tempo vamos brincar???'))
        for i,obj in enumerate(lista):
            lista[i].brincar()
        os.system('pause')
        
    elif opção == 3 :
        conversa= int(input('Ebaaaaa!!! Por quanto tempo vamos conversar???'))
        for i,obj in enumerate(lista):
            lista[i].ouvir()
        os.system('pause')

    elif opção == 4 :
        alt= int(input('Alterar a fome de qual Tamasgushi?(digite o número de identificação)'))
        lista[alt].AlterarFome()
        os.system('pause')
        
    elif opção == 5 :
        alt= int(input('Alterar a saúde de qual Tamasgushi?(digite o número de identificação)'))
        lista[alt].AlterarSaúde()
        os.system('pause')
        
    elif opção == 6 :
        alt= int(input('Alterar a idade de qual Tamasgushi?(digite o número de identificação)'))
        lista[alt].AlterarIdade()
        os.system('pause')
        
    elif opção == 7:
        alt= int(input('Alterar o nome de qual Tamasgushi?(digite o número de identificação)'))
        lista[alt].AlterarNome()
        os.system('pause')
        
    elif opção == 8 :
        print('Programa Finalizado')
        break
    
    else:
        os.system('cls')
        print('??????')
        print('você entrou no menu secreto!')
        print('------')
        for i,obj in enumerate(lista):
            print(f'{i} {obj.nome}- {obj.saude}-{obj.fome} {obj.tédio}')
        print('------')
        sleep(5)
        os.system('pause')
        os.system('cls')