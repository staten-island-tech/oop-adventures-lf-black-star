from hero import adventurer #TEMP

class shop:
    def __init__(self, equipment, potions, relics, rarity):
        self.equipment = equipment
        self.potions = potions
        self.relics = relics
        self.rarity = rarity
    
    def player_buy(self):
        prompt = input("What selection of items would you like to buy?")
        if prompt.isdigit() == False:
            print("Invalid input. Please try again.")
        else:
            prompt = int(prompt)
        if prompt == 1:
            print("equipment")
        if prompt == 2:
            print("Potions are one-time consumables that you can use during battle.")
        if prompt == 3:
            print("Relics are powerful permanent items that boost your stats.")

blacksmith = shop()