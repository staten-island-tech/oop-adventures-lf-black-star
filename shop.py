from hero import adventurer #TEMP
import random

class shop:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment
    
    def player_buy(self):
        Hprice = (random.randint((blacksmith.equipment[0] + 10), (blacksmith.equipment[0] + 15)) * 2)
        Cprice = (random.randint((blacksmith.equipment[1] + 15), (blacksmith.equipment[1] + 20)) * 2)
        Lprice = (random.randint((blacksmith.equipment[2] + 10), (blacksmith.equipment[2] + 15)) * 2)
        Bprice = (random.randint((blacksmith.equipment[3] + 5), (blacksmith.equipment[3] + 10)) * 2)
        Sprice = (random.randint((blacksmith.equipment[3] + 15), (blacksmith.equipment[3] + 20)) * 2)
        shop_equipment = blacksmith.equipment
        shop_equipment_text = ["helmet", "chestplate", "leggings", "boots", "sword"]
        prompt = "Not chosen!"
        while prompt != 2:
            print("1: View items")
            print("2: Leave shop")
            prompt = input(f"This is a {self.name}. What would you like to do?")
            if prompt.isdigit() == False:
                print("Invalid input. Please try again.")
            else:
                prompt = int(prompt)
                if prompt == 1:
                    print("Equipment provides an overall boost to your health, damage and defense in battle.")
                    if len(shop_equipment_text) == 0:
                        print("No equipment found!")
                    else:
                        print(shop_equipment)
                        selection = input(f"What would you like to purchase?")
                        selection = selection.lower()
                        if selection == "helmet" and selection in shop_equipment_text:
                            if adventurer.tokens >= Hprice:
                                adventurer.tokens -= Hprice
                            else:
                                print("You do not have enough tokens.")
                        if selection == "chestplate":
                            if adventurer.tokens >= Cprice:
                                adventurer.tokens -= Cprice
                            else:
                                print("You do not have enough tokens.")
                        if selection == "leggings":
                            if adventurer.tokens >= Lprice:
                                adventurer.tokens -= Lprice
                            else:
                                print("You do not have enough tokens.")
                        if selection == "boots":
                            if adventurer.tokens >= Bprice:
                                adventurer.tokens -= Bprice
                            else:
                                print("You do not have enough tokens.")
                        if selection == "sword":
                            if adventurer.tokens >= Sprice:
                                adventurer.tokens -= Sprice
                            else:
                                print("You do not have enough tokens.")
                if prompt == 2:
                    print(f"You left the {self.name}.")
                    return "player left"

blacksmith = shop("blacksmith", [random.randint((adventurer.ranking), (adventurer.ranking + 25)), random.randint((adventurer.ranking), (adventurer.ranking + 20)), random.randint((adventurer.ranking), (adventurer.ranking + 25)), random.randint((adventurer.ranking), (adventurer.ranking + 20)), random.randint((adventurer.ranking), (adventurer.ranking + 30))])
blacksmith.player_buy()
