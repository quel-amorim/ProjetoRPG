class Maestria:
    def __init__(self,nomeMaestria):
        self.nomeMaestria = nomeMaestria
        self.nivel = 1
        self.atributos = {
            'vitalidade' : 10,
            'forca' : 10,
            'defesa' : 10,
            'agilidade' : 10,
            'inteligencia' : 10
        }
        self.xpAtual = 0
        self.xpNivel = 100

    def exibirAtributos(self):
        print(f'------ Atributos {self.nomeMaestria} ----------')
        print(f'    VITALIDADE : {self.atributos['vitalidade']}')
        print(f'    FORCA : {self.atributos['forca']}')
        print(f'    DEFESA : {self.atributos['defesa']}')
        print(f'    AGILIDADE : {self.atributos['agilidade']}')
        print(f'    INTELIGENCIA : {self.atributos['inteligencia']}')
        print('---------------------------------------------------------\n')

class Lutador(Maestria):
    def __init__(self):
        super().__init__('Lutador')
        self.atributos['vitalidade'] +=2
        self.atributos['forca'] += 5
        self.atributos['defesa'] -= 3
        self.atributos['agilidade'] -= 2
        self.atributos['inteligencia'] -=5

class Mago(Maestria):
    def __init__(self):
        super().__init__('Mago')
        self.atributos['vitalidade'] -=1
        self.atributos['forca'] -= 5
        self.atributos['defesa'] += 1
        self.atributos['agilidade'] += 3
        self.atributos['inteligencia'] +=5

class Arqueiro(Maestria):
    def __init__(self):
        super().__init__('Arqueiro Safado')
        self.atributos['agilidade'] += 5
        self.atributos['inteligencia'] -=4

lutador = Lutador()

lutador.exibirAtributos()