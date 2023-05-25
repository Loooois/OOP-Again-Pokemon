class Pokemon:
    def __init__(self, Nam, Hel, Def, Att, Typ):
        self.name = Nam
        self.health = Hel
        self.defense = Def
        self.attack = Att
        self.type = Typ

    def printInfo(self):
        print("Name is {} with {} health, {} as defense, {} for attack and {} type.".format(self.name, self.health, self.defense, self.attack, self.type))
    
    def uniqueMove(self):
        print("generic move sound, cant wait to be overrid thwack")

class Pokemon_Fire(Pokemon):
    def __init__(self, Nam, Hel, Def, Att, Typ):
        super().__init__(Nam, Hel, Def, Att + 10, Typ)
    
    def printInfo(self):
        print("*sizzles* Name is {} with extra 我黑 {} health, {} as defense, {} for attack and {} type.".format(self.name, self.health, self.defense, self.attack, self.type))

    def uniqueMove(self):
        print("AMAMMAMAMZING FLAME GUN")

class Pokemon_Grass(Pokemon):
    def __init__(self, Nam, Hel, Def, Att, Typ):
        super().__init__(Nam, Hel + 5, Def + 5, Att, Typ)

    def printInfo(self):
        print("*shshshshshshhshs* Name is {} with extra 树叶 {} health, {} as defense, {} for attack and {} type.".format(self.name, self.health, self.defense, self.attack, self.type))

    def uniqueMove(self):
        print("NOBODY LIKE GRES")

class Pokemon_H2O(Pokemon):
    def __init__(self, Nam, Hel, Def, Att, Typ):
        super().__init__(Nam, Hel + 5, Def, Att + 5, Typ)

    def printInfo(self):
        print("*咕咚咕咚咕咚咕咚咕咚咕咚咕咚咕咚* Name is {} with extra 蒸馏水 {} health, {} as defense, {} for attack and {} type.".format(self.name, self.health, self.defense, self.attack, self.type))

    def uniqueMove(self):
        print("WATER GUN (GOOFY AHH VERSON OF AMAMMAMAMZING FLAME GUN)")

bulba = Pokemon_Grass("Bull", 100, 10, 15, "gras")
charm = Pokemon_Fire("Wok Hei", 80, 15, 25, "Fair")
squirt = Pokemon_H2O("Squirt", 60, 40, 20, "WADDER")

print(bulba.printInfo())
print(charm.printInfo())
print(squirt.printInfo())

print(bulba.uniqueMove())
print(charm.uniqueMove())
print(squirt.uniqueMove())


#haibrid inheritencne

class betel(Pokemon_Grass, Pokemon_Fire, Pokemon_H2O):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def P1att(self):
        self.p2.Hel -= (self.p1.Att*2)-self.p2.Def

    def P2att(self):
        self.p1.Hel -= (self.p2.Att*2)-self.p1.Def

battle1 = betel(bulba, charm)
betel.P1att()
betel.P2att()