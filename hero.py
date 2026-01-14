class Hero:
    def __init__(self, health, damage, inventory, tokens, relics, speed, regen, weapon, chestplate, helmet, leggings, boots, ranking):
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.tokens = tokens
        self.relics = relics
        self.speed = speed
        self.regen = regen
        self.weapon = weapon
        self.chestplate = chestplate
        self.helmet = helmet
        self.leggings = leggings
        self.boots = boots
        self.ranking = ranking

    def apply_boosts(self):
        self.health += (self.chestplate + self.helmet + self.leggings + self.boots)
        self.damage += self.weapon
    
    def attack(self):
        print("yay")

adventurer = Hero(100, 20, [], 0, [], 1, 0, 5, 10, 5, 5, 5, 0)
