from hero import adventurer #TEMP

class shop:
    def __init__(self, equipment, potions, relics, rarity):
        self.equipment = equipment
        self.potions = potions
        self.relics = relics
        self.rarity = rarity
    
    def player_buy(self):
        prompt = input("")