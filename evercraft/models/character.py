# this is where your character code will go
import math
class Character:
    name = "Evercraft",
    alignment = "neutral",
    AC = 10
    base_hp = 5
    HP = 5
    life = True
    str = 10
    dex = 10
    int = 10
    wis = 10
    cha = 10
    con = 10
    XP = 0
    level = 1
    #object that stores the default values for a new character
    DEFAULT: {
        "name": "Evercraft",
        "alignment": "neutral",
        "AC": 10,
        "HP": 5,
        "life": True,
        "str": 10,
        "dex": 10,
        "int": 10,
        "wis": 10,
        "cha": 10,
        "con": 10,
        "XP": 0,
        "level": 1,
        "base_hp":5
    }
    
    def __init__(self, obj={}):
        #for each key in the obj
        for key in obj:
            #if there is an appropriate key
            if key in obj:
                #set the attribute to the one in the key that was established
                setattr(self, key, obj[key])
            #otherwise
            else:
                #set them to the values in the default object.
                setattr(self, key, self.DEFAULT[key])
        #set the armor class using the set_AC method.  Do the same for the set HP method
        self.AC = self.set_AC(self.dex)
        self.HP = self.set_HP(self.con)
        self.check_XP(self.XP)
    #this isn't strictly necessary, since you can set the value without it.
    def set_name(self, name):
        self.name = name
    #same for this
    def get_name(self):
        return self.name
    #attack method
    #this handles attacks, damage, xp on sucessful attack, checking for level up
    def attack(self, target, roll, score):
        #creates a mod for the attack roll
        mod = self.modify(score)
        #base damage and the modifier established earlier
        damage = 1 + mod
        #a second modifier based on the level
        mod_level = (math.floor(self.level/2))
        #check for a crit first
        if roll == 20:
            #add XP, then check for a level up
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            #if, for any reason, the damage output is less than one, make it one instead
            if damage < 1:
                damage = 1
            #reduce the target's HP based on the damage output
            target.HP = target.HP - (damage*2)
            #check if their HP was reduced to 0, and switch their life boolean to false if they are.
            if target.HP <= 0:
                target.life = False
            return 'Hit'
        elif roll + mod + mod_level >= target.AC:
            self.XP = self.XP + 10
            self.check_XP(self.XP)
            if damage < 1:
                damage = 1
            target.HP = target.HP - damage
            if target.HP <= 0:
                target.life = False
            return "Hit"
        elif roll + mod + mod_level < target.AC:
            return "Whiff"
        else:
            return "That doesn't seem to be a number"
        self.check_XP(self.XP)

    def modify(self, score):
        switcher = {
            20: 5,
            19: 4,
            18: 4,
            17: 3,
            16: 3,
            15: 2,
            14: 2,
            13: 1,
            12: 1,
            11: 0,
            10: 0,
            9: -1,
            8: -1, 
            7: -2,
            6: -2,
            5: -3,
            4: -3,
            3: -4,
            2: -4,
            1: -5
        }
        return switcher.get(score)
    
    ##We want to call these when a character is created, at level up, and equipment(stretch)
    ##they also will probably want to be merged into a unified function later
    def set_AC(self, score):
        return max(1, self.AC + self.modify(score))

    def set_HP(self, score):
        print('character set hp')
        return max(1, self.base_hp * self.level + self.modify(score)*self.level)

    #this function probably should be called whenever a xp changes
    def check_XP(self, XP):
        self.level = (math.floor(self.XP/1000))+1

##############
#End of Class#
##############
##some non-default traits to work with
example_traits = {
    "name": "Rufus",
    "alignment": 'good',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str": 12,
    "dex": 14,
    "int": 10,
    "wis": 10,
    "cha": 10,
    "con": 14,
    "XP": 0,
    "level":1
}
Rufus = Character(example_traits)
c2 = Character()
bad_guy = {
    "name": "Evil Rufus",
    "alignment": 'evil',
    "AC": 12,
    'HP': 8,
    "life": True,
    "str": 10,
    "dex": 10,
    "int": 10,
    "wis": 10,
    "cha": 10,
    "con": 10,
    "XP": 0
}
bad_guy = Character(bad_guy)
print(Rufus.level)
Rufus.attack(bad_guy, 20, Rufus.str)
print(Rufus.level)
##default character
# print(c1.AC)
