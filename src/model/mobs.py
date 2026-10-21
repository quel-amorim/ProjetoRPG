from random import randint
class Mobs:
    def __init__(self,nome):
        self.nome = nome
        self.nivel = 1
        self.atributos = { # Atributos para mobs padrão
            'vitalidade' : 10,
            'forca' : 10,
            'defesa' : 10,
            'agilidade' : 10,
            'inteligencia' : 10
        }
        self.xpAtual = 0
        self.xpUp = 100

    def uparNivel(self):
        if self.xpAtual >= self.xpUp:
            print(f'{self.nome} UPOU DE NIVEL')
            self.nivel += 1
            self.xpUp += 150
            self.xpAtual = 0 # toda vez que upar vai deixar o xp atual em 0


    def chanceDrops(self):
        itensDrop = []
        xpRecibido = randint(1, 10)
        moedasRecibidas = randint(1,50)
    
    def exibirAtributos(self):
        print(f"Atributos {self.nome}")
        print('-'*40)
        print(f"VITALIDADE : {self.atributos['vitalidade']}")
        print(f"FORÇA : {self.atributos['forca']}")
        print(f"DEFESA : {self.atributos['defesa']}")
        print(f"AGILIDADE : {self.atributos['agilidade']}")
        print(f"INTELIGENCIA : {self.atributos['inteligencia']}")

class Zumbi(Mobs):
    def __init__(self):
        super().__init__("Zumbi")
        self.atributos['vitalidade'] = 7
        self.atributos['agilidade'] = 3
        self.atributos['inteligencia'] = 1
        self.atributos['defesa'] = 3

class Demonio(Mobs):
    def __init__(self):
        super().__init__("Demônio")
        self.atributos['vitalidade'] += 3
        self.atributos['forca'] += 5
        self.atributos['defesa'] += 1
        self.atributos['agilidade'] += 3
        self.atributos['inteligencia'] +=4

