from random import choices,randint
class Mob:
    def __init__(self,nomeMob,elemento,vitalidade,forca,defesa,agilidade,inteligencia):
        self.nomeMob = nomeMob
        self.nivel = 1
        self.elemento = elemento
        self.atributo = {
            "vitalidade" : vitalidade,
            "forca" : forca,
            "defesa" : defesa,
            "agilidade" : agilidade,
            "inteligencia" : inteligencia
        }
        self.hpMax = 10 * self.atributo["vitalidade"]
        self.hpMin = 2 / (self.hpMax * 5)
        self.danoMax = 10 * self.atributo["forca"]
        self.danoMin = 2 / (self.danoMax * 5)
        self.restencia = 10 * self.atributo["defesa"]
        self.velocidade = 10 * self.atributo["agilidade"]
        self.mental = 10 * self.atributo["inteligencia"]
        self.valoresStatus = {
            "hpMax" : self.hpMax,
            "hpMin" : self.hpMin,
            "danoMax" : self.danoMax,
            "danoMin" : self.danoMin,
            "resistencia" : self.restencia,
            "velocidade" : self.velocidade,
            "mental" : self.mental
        }
        self.geraRaridades()
        self.moedas = randint(1 , 50)
        self.xp = randint(1 ,50)
        self.chancesDrop()

    def geraRaridades(self):
        niveisRaridades = ["Normal","Raro","Lendário"]
        raridade = choices(niveisRaridades,weights=[50,40,10],k=1)[0]
        if raridade == "Raro":
            self.atributo["vitalidade"] +=1
            self.atributo["forca"] +=1
            self.atributo["defesa"] +=1
            self.atributo["agilidade"] +=1
            self.atributo["inteligencia"] +=1
            print("MOB RARO + 1 EM TODOS ATRIBUTOS")
            return self.atributo
        elif raridade == "Lendário":
            self.atributo["vitalidade"] +=3
            self.atributo["forca"] +=3
            self.atributo["defesa"] +=3
            self.atributo["agilidade"] +=3
            self.atributo["inteligencia"] +=3
            print("MOB LENDÁRIO + 3 EM TODOS OS ATRIBUTOS")
            return self.atributo

        return raridade

    def chancesDrop(self):
        drops = ["Machado","Arco","Espada","Essencia da Monstro"]
        drop = choices(drops , weights=[10,10,10,70])
        return drop

    def exibirAtributos(self):
        print(f""" {self.nomeMob}
===========================================
    VIT : {self.atributo["vitalidade"]}
    STR : {self.atributo["forca"]}
    RES : {self.atributo["defesa"]}
    AGI : {self.atributo["agilidade"]}
    INT : {self.atributo["inteligencia"]}
""")

    def exibirStatus(self):
        print(f"  HP :{self.valoresStatus["hpMax"]}/ {self.valoresStatus["hpMin"]}")
        print(f"  DANO : {self.valoresStatus["danoMax"]} / {self.danoMin}")
        print(f"  RESISTENCIA : {self.valoresStatus["resistencia"]}")
        print(f"  VELOCIDADE : {self.valoresStatus["velocidade"]}")
        print(f"  MENTAL : {self.valoresStatus["mental"]}")

    def __repr__(self):
        return f" * MOB {self.nomeMob} Nv {self.nivel}"

zumbi = Mob("ZUMBI","TERRA",5,10,5,2,1)
demonio = Mob("DEMONIO","TREVAS",11,14,10,12,10)
anjo = Mob("ANJO","LUZ",12,14,10,13,12)

zumbi.exibirStatus()

#ARRUMAR DEPOIS OS VALORES DO STATUS