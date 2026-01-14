
class Hero:
    def __init__(self, health, damage, inventory, tokens, relics, speed, regen, wealth, weapon, helmet, chestplate, leggings, boots):
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.tokens = tokens
        self.relics = relics
        self.speed = speed
        self.regen = regen
        self.wealth = wealth
        self.weapon = weapon
        self.chestplate = chestplate
        self.helmet = helmet
        self.leggings = leggings
        self.boots = boots
    
    def attack(self):
        print("yay")

adventurer = Hero(100, [], 0, [], 1, 0)
