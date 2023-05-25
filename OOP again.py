# class pokemon:
#     def __init__(self, name, hp, atk, defn):
#         self.__name = name
#         self.__hp = hp
#         self.__atk = atk
#         self.__defn = defn

    #gggeeettt
    # def whodatdpomon(self):
    #     return self.__name
    
    # def hawstrongru(self):
    #     return self.__atk
    
    # def brusotenki(self):
    #     return self.__hp
    
    # def waicantdodmgtou(self):
    #     return self.__defn
    
#     #ssseeettt
#     def reenem(self, neeewnem):
#         self.__name = neeewnem

#     def omagodneedtorun(self, waideheluatek):
#         self.__hp -= waideheluatek
    
#     def lesgoistronkhahayoudai(self, omagodimaginigetstronger):
#         self.__atk += omagodimaginigetstronger

#     def igotdmgreductionimagineskillissue(self, defngobrrrr):
#         self.__defn += defngobrrrr


# pokemon1 = pokemon("May 4th", 10000, 10000, 10000)
# print(pokemon1.whodatdpomon())
# pokemon1.reenem("March 7th")
# print(pokemon1.whodatdpomon())

# class sheetpokemoncard:
#     def __init__(self, nem, skil):
#         self.__nem = nem
#         self.skil = skil

# pokemon2 = sheetpokemoncard("bad", "issue")
# pokemon2.__nem = "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
# print(pokemon2.__dict__)



class pokemon:
    __turn = 1
    def __init__(self, name, hp, atk, defn):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__defn = defn
        self.__lvl = 1
        self.__xp = 0

        self.__maxhp = self.__hp * self.__lvl
        self.__regatk = self.__atk * self.__lvl
        self.__regdefn = self.__defn * self.__lvl

    def poke_info(self):
        return "{} level {}: \n\thealth = {}/{} \n\tattack = {} \n\tdefence = {}".format(self.__name,self.__lvl,self.__hp,self.__maxhp,self.__atk,self.__defn)

    # def attack(opponent, self):
    #     opponent.__hp -= self.__atk

    # def debuff(opponent, self):
    #     opponent.__defn -= self.__lvl * 100
    #     opponent.__atk -= self.__lvl * 100

    # get all basic attribute
    def getName(self):
        return self.__name
    
    def getAtk(self):
        return self.__atk
    
    def getHP(self):
        return self.__hp
    
    def getDef(self):
        return self.__defn
    
    def getLvl(self):
        return self.__lvl
    
    def getXP(self):
        return self.__xp

    def attack(self, deff):
        if (self.__atk - deff) > 0:
            return(self.__atk - deff)
        else:
            return 0
    
    def took_dmg(self, dmg_taken):
        self.__hp = self.__hp - dmg_taken

    def buffdefn(self):
        self.__defn = self.__defn * 2

    def buffatk(self):
        self.__atk = self.__atk * 2

    def heal(self):
        self.__hp = self.__hp * 2

pokemon1= pokemon("ViperSRT", 1000, 150, 1000)    
pokemon2= pokemon("SSCTuatara", 100, 1000, 100)
print(pokemon1.poke_info())
print(pokemon2.poke_info())


pokemon2.took_dmg(pokemon1.attack(pokemon2.getDef()))

print(pokemon2.poke_info())