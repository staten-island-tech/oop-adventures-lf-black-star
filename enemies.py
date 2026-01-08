class Enemy:
    def __init__(self, health, damage, defense, tokens, relic_chance, difficulty):
        self.health = health
        self.damage = damage
        self.defense = defense
        self.tokens = tokens
        self.relic_chance = relic_chance
        self.difficulty = difficulty #might not be necessary but idk
    
    def attack(self):
        