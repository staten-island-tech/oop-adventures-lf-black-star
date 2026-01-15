from hero import adventurer #TEMP
import random

class shop:
    def __init__(self, name, equipment):
        self.name = name
        self.equipment = equipment
    
    def prepare_shop(self):
        if self.name == "blacksmith":
            global blacksmith_items
            blacksmith_items = [{"name": "Helmet", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)), "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{"name": "Chestplate", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)), "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}
    ,{"name": "Leggings", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)), "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{"name": "Boots", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)), "price": (random.randint((adventurer.ranking + 5), (adventurer.ranking + 10)) * 2)}
    ,{"name": "Sword", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 30)), "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}]
            blacksmith.player_interact()
    
    def player_interact(self):
        prompt = "Not decided."
        while prompt != 3:
            item_names = [item["name"] for item in blacksmith_items]
            confirm = "Not decided."
            print("1: View items")
            print("2: Sell items")
            print("3: Leave shop")
            prompt = input(f"This is a {self.name}. What would you like to do?")
            if not prompt.isdigit():
                print("Invalid input. Please try again.")
                continue
            prompt = int(prompt)
            if prompt not in [1, 2, 3]:
                print("Invalid input. Please try again.")
            if prompt == 1:
                for index, i in enumerate(blacksmith_items, start = 1):
                    print(index, ":", i)
                selection = input(f"What would you like to purchase?")
                if not selection.isdigit():
                    print("Invalid input. Please try again.")
                    continue
                selection = int(selection) - 1
                if adventurer.tokens < blacksmith_items[selection]["price"]:
                      print("You do not have enough tokens.")
                      continue
                adventurer.tokens -= blacksmith_items[selection]["price"]
                print(f"Purchase successful! Current token balance: {adventurer.tokens}")
                while confirm not in ["y" or "yes" or "n" or "no"]:
                      confirm = input("Would you like to equip your new item?")
                      confirm = confirm.lower()
                      if confirm in ["y" or "yes"]:
                            adventurer.equipment[selection]["boost"] = blacksmith_items[selection]["boost"]
                            adventurer.equipment[selection]["price"] = blacksmith_items[selection]["price"]
                            print("Item equipped.")
                            print(adventurer.equipment)
                            
                            continue
                      if confirm in ["n" or "no"]:
                            print("Item added to inventory.")
                            adventurer.inventory.append(blacksmith_items[selection])
                            print(adventurer.inventory)
                            continue
                      else:
                          print("Invalid input. Please try again.")

            if len(item_names) <= 0:
                print("No items found!")
            elif prompt == 2:
                if len(adventurer.inventory) <= 0:
                    print("Nothing is in your inventory.")
                    continue
                print("Your inventory:")
                for index, i in enumerate(adventurer.inventory, start = 1):
                    print(index, ":", i)
                    sell_choice = input("What item would you like to sell?")
                    if not sell_choice.isdigit():
                        print("Invalid input. Please try again.")
                        continue
                    sell_choice = int(sell_choice) - 1
                    if sell_choice not in adventurer.inventory:
                        print("Invalid input. Please try again.")
                        continue
                    adventurer.tokens += adventurer.inventory[sell_choice]["price"]
                    print(f"Sold item successfully! {adventurer.inventory[sell_choice]["price"]} tokens earned.")
                    del adventurer.inventory[sell_choice]
            elif prompt == 3:
                print(f"You left the {self.name}.")
                #call function HERE
                return



blacksmith_items = [{"name": "Helmet", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)), "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{"name": "Chestplate", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)), "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}
    ,{"name": "Leggings", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 25)), "price": (random.randint((adventurer.ranking + 10), (adventurer.ranking + 15)) * 2)}
    ,{"name": "Boots", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 20)), "price": (random.randint((adventurer.ranking + 5), (adventurer.ranking + 10)) * 2)}
    ,{"name": "Sword", "boost": random.randint((adventurer.ranking), (adventurer.ranking + 30)), "price": (random.randint((adventurer.ranking + 15), (adventurer.ranking + 20)) * 2)}]
blacksmith = shop("blacksmith", blacksmith_items)
print((adventurer.inventory))
blacksmith.prepare_shop()