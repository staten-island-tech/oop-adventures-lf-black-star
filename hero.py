class Hero:
    def __init__(self, health, defense, damage, inventory, tokens, relics, speed, regen, weapon, chestplate, helmet, leggings, boots):
        self.health = health
        self.defense = defense
        self.damage = damage
        self.inventory = inventory
        self.tokens = tokens
        self.relics = relics
        self.speed = speed
        self.regen = regen
    
    def attack(self):
        print("yay")

adventurer = Hero(100, 0, 20, [], 0, [], 1, 0)