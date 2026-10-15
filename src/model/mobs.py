from random import choices, randint

class Mob:
    def __init__(self, nomeMob, vitalidade, forca, defesa, agilidade, inteligencia):
        self.nomeMob = nomeMob
        self.nivel = 1
        self.atributo = {
            "vitalidade": vitalidade,
            "forca": forca,
            "defesa": defesa,
            "agilidade": agilidade,
            "inteligencia": inteligencia
        }
        
        self.raridade = self.geraRaridades()
        
        self.hp_maximo = self.atributo["vitalidade"] * 10
        self.hp_atual = self.hp_maximo  # Começa com a vida cheia
        
        self.dano_fisico = int(self.atributo["forca"] * 2.5)
        self.defesa_total = self.atributo["defesa"] * 2
        self.velocidade = self.atributo["agilidade"] * 3
        self.poder_magico = self.atributo["inteligencia"] * 4
        
        # Outras propriedades
        self.moedas = randint(1, 50)
        self.xp = randint(1, 50)
        self.drop = self.chancesDrop()

    def geraRaridades(self):
        niveisRaridades = ["Normal", "Raro", "Lendário"]
        raridade = choices(niveisRaridades, weights=[50, 40, 10], k=1)[0]
        
        if raridade == "Raro":
            for k in self.atributo:
                self.atributo[k] += 1
            print(f"[{self.nomeMob}] MOB RARO! +1 em todos os atributos.")
        elif raridade == "Lendário":
            for k in self.atributo:
                self.atributo[k] += 3
            print(f"[{self.nomeMob}] MOB LENDÁRIO! +3 em todos os atributos.")
            
        return raridade

    def chancesDrop(self):
        drops = ["Machado", "Arco", "Espada", "Essência do Monstro"]
        return choices(drops, weights=[10, 10, 10, 70])[0]

    def exibirAtributos(self):
        print(f""" {self.nomeMob} ({self.raridade}) - Nv {self.nivel}
===========================================
    VIT : {self.atributo["vitalidade"]}
    STR : {self.atributo["forca"]}
    DEF : {self.atributo["defesa"]}
    AGI : {self.atributo["agilidade"]}
    INT : {self.atributo["inteligencia"]}
""")

    def exibirValoresStatus(self):
        print(f"""--- Status de Combate: {self.nomeMob} ---
    HP          : {self.hp_atual}/{self.hp_maximo}
    Dano Físico : {self.dano_fisico}
    Defesa      : {self.defesa_total}
    Velocidade  : {self.velocidade}
    Poder Mágico: {self.poder_magico}
----------------------------------------
""")

    def __repr__(self):
        return f" * MOB {self.nomeMob} ({self.raridade}) Nv {self.nivel}"


zumbi = Mob("ZUMBI",5, 10, 5, 2, 1)
zumbi.exibirAtributos()
zumbi.exibirValoresStatus()