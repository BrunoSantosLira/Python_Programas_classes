class Tv:
    def __init__(self, canal=30, Volume=100):
        self.canal= canal
        self.volume= Volume
        
        
    def mudarCanal(self):
        while True:
            Mude= int(input('Para qual canal deseja mudar?(Existe até o 30³ canal no seu pacote)'))
            if Mude > 30:
                print(f'Esse canal não está no seu pacote')
            elif Mude < 0:
                print('Não existe canal abaixo de 0')
            else:
                self.canal= Mude
                print(f'Mudado para o canal {Mude} com sucesso!')
                break
    
    
    def mudarVolume(self):
        while True:
            Volume= int(input('Para qual volume deseja alterar?(volume máximo:100)'))
            if Volume > 100:
                print('Impossível elevar o volume a 100% !')
            elif Volume < 0:
                print('Impossível alterar o volume para abaixo de 0')
            else:
                self.volume = Volume
                print(f'Volume alterado para {Volume}% com sucesso!')
                break
        
        
        
Tv1= Tv()
Tv1.mudarCanal()
print(Tv1.canal)
print('----------------')
print(Tv1.volume)
Tv1.mudarVolume()
print(Tv1.volume)
        