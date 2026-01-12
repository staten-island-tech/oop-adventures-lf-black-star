from hero import adventurer #TEMP
import random

class shop:
    def __init__(self, name, equipment, potions):
        self.name = name
        self.equipment = equipment
        self.potions = potions
    
    def player_buy(self):
        prompt = input("What selection of items would you like to buy?")
        if prompt.isdigit() == False:
            print("Invalid input. Please try again.")
        else:
            prompt = int(prompt)
        if prompt == 1:
            print("Equipment provides an all-around boost to your health, damage and defense in battle.")
        if prompt == 2:
            print("Potions are one-time consumables that you can use during battle.")

blacksmith = shop("Blacksmith", [adventurer.helmet, adventurer.chestplate, adventurer. leggings, adventurer.boots, adventurer.weapon], [], )
shop_list = [blacksmith, ]