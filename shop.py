from hero import adventurer #TEMP
import random

class shop:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment
    
    def prepare_shop(self):
        if self.name == "blacksmith":
            global blacksmith_items
            blacksmith_items = [{
        "name": "Helmet",
        "stat boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)),
        "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{
        "name": "Chestplate",
        "stat boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)),
        "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}
    ,{
        "name": "Leggings",
        "stat boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)),
        "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{
        "name": "Boots",
        "stat boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)),
        "price": (random.randint((adventurer.ranking + 5), (adventurer.ranking + 10)) * 2)}
    ,{
        "name": "Sword",
        "stat boost": random.randint((adventurer.ranking), (adventurer.ranking + 30)),
        "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}]
            blacksmith.player_interact()
    
    def player_interact(self):
        item_names = [item["name"] for item in blacksmith_items]
        prompt = "Not chosen!"
        while prompt != 3:
            print("1: View items")
            print("2: Sell items")
            print("3: Leave shop")
            prompt = input(f"This is a {self.name}. What would you like to do?")
            if prompt.isdigit() == False:
                print("Invalid input. Please try again.")
            else:
                prompt = int(prompt)
                if prompt == 1 and len(item_names) > 0:
                    print("Equipment provides an overall boost to your health, damage and defense in battle.")
                    for index, item in enumerate(blacksmith_items, start = 1):
                        print(index, ":", item)
                    selection = input(f"What would you like to purchase?")
                    if selection in item_names:
                        if selection == 1:
                            if adventurer.tokens >= blacksmith_items[0]["price"]:
                                adventurer.tokens -= blacksmith_items[0]["price"]
                                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                            else:
                                print("You do not have enough tokens.")
                        if selection == 2:
                            if adventurer.tokens >= blacksmith_items[1]["price"]:
                                adventurer.tokens -= blacksmith_items[1]["price"]
                                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                            else:
                                print("You do not have enough tokens.")
                        if selection == 3:
                            if adventurer.tokens >= blacksmith_items[2]["price"]:
                                adventurer.tokens -= blacksmith_items[2]["price"]
                                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                            else:
                                print("You do not have enough tokens.")
                        if selection == 4:
                            if adventurer.tokens >= blacksmith_items[3]["price"]:
                                adventurer.tokens -= blacksmith_items[3]["price"]
                                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                            else:
                                print("You do not have enough tokens.")
                        if selection == 5:
                            if adventurer.tokens >= blacksmith_items[4]["price"]:
                                adventurer.tokens -= blacksmith_items[4]["price"]
                                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                            else:
                                print("You do not have enough tokens.")
                        else:
                            print("Invalid input. Please try again.")
                else:
                    print("No items found!")
                if prompt == 2:
                    print("soon")
                if prompt == 3:
                    print(f"You left the {self.name}.")
                    return "player left"

blacksmith_items = [{
        "name": "Helmet",
        "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)),
        "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{
        "name": "Chestplate",
        "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)),
        "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}
    ,{
        "name": "Leggings",
        "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)),
        "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{
        "name": "Boots",
        "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)),
        "price": (random.randint((adventurer.ranking + 5), (adventurer.ranking + 10)) * 2)}
    ,{
        "name": "Sword",
        "boost": random.randint((adventurer.ranking), (adventurer.ranking + 30)),
        "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}]
blacksmith = shop("blacksmith", blacksmith_items)
blacksmith.prepare_shop()
