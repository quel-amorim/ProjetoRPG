class Maestria:
    def __init__(self,nomeMaestria,elemento,vitalidade,forca,defesa,agilidade,inteligencia):
        self.nomeMaestria = nomeMaestria
        self.elemento = elemento
        self.nivel = 1
        self.vitalidade = vitalidade
        self.forca = forca
        self.defesa = defesa
        self.agilidade = agilidade
        self.inteligencia = inteligencia
        self.exp = 0

    def exibirAtributos(self):
        return f"""
    VIT : {self.vitalidade}
    STR : {self.forca}
    RES : {self.defesa}
    AGI : {self.agilidade}
    INT : {self.inteligencia}
"""

    def __repr__(self):
        return f"{self.nomeMaestria} Nv {self.nivel}\nElemento :{self.elemento}\n{self.exibirAtributos()}\nBarra de Exp : {self.exp}"

lutador = Maestria("LUTADOR","TERRA",10,15,10,7,5)
mago = Maestria("MAGO","FOGO",10,10,12,13,15)
arqueiro = Maestria("ARQUEIRO","VENTO",10,14,10,15,10)

print(lutador)