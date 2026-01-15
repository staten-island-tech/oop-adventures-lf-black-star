from equipment import hermes
from equipment import aphrodite
from equipment import plutus
from equipment import athena
from equipment import ares
class Hero:
    def __init__(self, health, damage, inventory, tokens, obtained_relics, speed, regen, wealth, weapon, helmet, chestplate, leggings, boots, ranking):
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.tokens = tokens
        self.obtained_relics = obtained_relics
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
        if hermes in self.obtained_relics:
            self.speed += hermes.stat_boost
        if aphrodite in self.obtained_relics:
            self.regen += aphrodite.stat_boost
        if plutus in self.obtained_relics:
            self.wealth += plutus.stat_boost
        if athena in self.obtained_relics:
            self.weapon += athena.stat_boost
        if ares in self.obtained_relics:
            self.damage += ares.stat_boost
        self.health += (self.chestplate + self.helmet + self.leggings + self.boots)
        self.damage += self.weapon
    
    def attack(self):
        print("yay")

adventurer = Hero(100, 20, [], 999999999, {
        "name": "Blessing of Hermes",
        "is_obtained": False}
    ,{
        "name": "Blessing of Aphrodite",
        "is_obtained": False}
    ,{
        "name": "Blessing of Plutus",
        "is_obtained": False}
    ,{
        "name": "Blessing of Athena",
        "is_obtained": False}
    ,{
        "name": "Blessing of Ares",
        "is_obtained": False} , 1, 0, 1, 5, 10, 5, 5, 5, 0)
print(adventurer)