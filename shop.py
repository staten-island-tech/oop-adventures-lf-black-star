from hero import adventurer #TEMP
import random

class shop:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment
    
    def player_buy(self):
        prompt = "Not chosen!"
        while prompt != 2:
            prompt = input(f"This is a {self.name}. What equipment would you like to purchase?")
            if prompt.isdigit() == False:
                print("Invalid input. Please try again.")
            else:
                prompt = int(prompt)
            if prompt == 1:
                print("Equipment provides an all-around boost to your health, damage and defense in battle.")
                print(f"Helmet: +{self.equipment[0]} health. Chestplate: +{self.equipment[1]} health. Leggings: +{self.equipment[2]} health. Boots: +{self.equipment[3]} health.")
                if len(self.equipment) == 0: #make weapon
                    print("No equipment found!")
            if prompt == 2:
                print(f"You left the {self.name}.")
                return

blacksmith = shop("blacksmith", [random.randint((adventurer.helmet), (adventurer.helmet + 25)), random.randint((adventurer.chestplate), (adventurer.chestplate + 20)), random.randint((adventurer.leggings), (adventurer.leggings + 25)), random.randint((adventurer.boots), (adventurer.boots + 20)), random.randint((adventurer.weapon), (adventurer.weapon + 30))])
blacksmith.player_buy()
