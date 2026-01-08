import random

class Enemy:
    def __init__(self, name, health, damage, defense, token_drops, relic_chance, difficulty):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.token_drops = token_drops
        self.relic_chance = relic_chance
        self.difficulty = difficulty #might not be necessary but idk
    
    def attack(self):
        adventurer.health - self.damage
        print(adventurer.health)
    
    def dealt_damage(self):
        self.health - adventurer.damage
        if self.health <= 0:
            print(f"{self.name} slain! {self.token_drops} tokens rewarded.")
            adventurer.tokens += self.token_drops
            if self.relic_chance >= random.randint(1, 100):
                
        
