class Hero:
    def __init__(self, health, damage, inventory, tokens, relics, speed, regen, wealth, weapon, helmet, chestplate, leggings, boots, ranking):
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.tokens = tokens
        self.relics = relics
        self.speed = speed
        self.regen = regen
        self.wealth = wealth
        self.weapon = weapon
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.ranking = ranking

    def apply_boosts(self):

        self.health += (self.chestplate + self.helmet + self.leggings + self.boots)
        self.damage += self.weapon
    
    def attack(self):
        print("yay")

adventurer = Hero(100, 20, [], 0, [], 1, 0, 1, 5, 10, 5, 5, 5, 0)