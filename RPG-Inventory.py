# CS 30 RPG Inventory Assignment
# Catherine McLellan
# October 5, 2021
import random
# Starting inventory for player:
inventory = {"potions": 0, "elixirs": 0, "weapons": []}
party = ["Yourself"]

# Player stats at beginning of the game:
health = 2
max_health = 2
attack = 0
gold = 0

# Listing weapons, healing items, characters, and locations in the game:
weapon = {
    "Rusty knife":
    {
        "Description: ": "A puny knife that has rusted over.",
        "Price: ": "Costs 1 gold"},
    "Pocket knife":
    {
        "Description: ": "A tiny blade. Looks like a letter opener.",
        "Price:": "Costs 2 gold"},
    "Dagger":
    {
        "Description: ": "Slightly better than a pocket knife.",
        "Price: ": "Costs 5 gold"},
    "Healing sword":
    {
        "Description: ": "Upgraded rusty knife, heals you when you fight!",
        "Price: ": "Costs 20 gold and requires the rusty knife."},
    "Rusty broadsword":
    {
        "Description: ": "Looks really old but still has some fight left.",
        "Price: ": "Costs 8 gold"},
    "Broadsword":
    {
        "Description: ": "A hero's sword.",
        "Price: ": "Costs 15 gold"}
    }

healing_stuff = {
    "Potion":
    {"Description: ": "Heals one health.",
        "Cost: ": "5 gold."},
    "Elixir":
    {"Description: ": "Adds to maximum health.",
        "Cost: ": "15 gold."}
}


characters = {
    "Frail Woman":
    {
        "Description: ": "She's very frail, but she will do her best to help.",
        "Stats: ": "Attack increases by 2, Max health increases by 2"},
    "Glogo":
    {
        "Description: ":
        """A squat, grey-skinned creature with round, red eyes,
and rows of spikes on its back.
        """,
        "Stats: ": "Attack increases by 3, Max health increases by 1"},
    "Cat":
    {
        "Description: ":
        "A massive, blue cat that looks like it wants to eat you.",
        "Stats: ": "Attack increases by 4"}
}

locations = {
    "Gold": "You found some gold!",
    "Monster": "Fight a goblin!",
    "Witch": "Witch steals a health!",
    "Market": "Purchase weapons or healing items!",
    "New ally!": "New character joins party!"
}
player_options = "1. Explore", "2. See inventory", "3. Heal", "4. Quit"


def see_inventory():
    """Displays inventory, party, and player status"""
    if inventory == [[0, 0], []]:
        print("You don't have any healing items or weapons!")
    elif inventory != [[0, 0], []]:
        total_potions = f"""You have {inventory["potions"]} potions and """
        total_elixirs = f"""{inventory["elixirs"]} elixirs."""
        if inventory["potions"] == 1:
            total_potions = f"""You have {inventory["potions"]} potion and """
        if inventory["elixirs"] == 1:
            total_elixirs = f"""{inventory["elixirs"]} elixir."""
        print(total_potions + total_elixirs)
        if inventory["weapons"] == []:
            print("""You have no weapons!""")
        for weapon in inventory["weapons"]:
            print(f"""You have a {weapon}.""")
    print("""Your party: """ + ", ".join(map(str, party)))
    print("Your total attack is " + str(attack) + ".")
    print("You have " + str(gold) + " gold.")
    print("You have " + str(health) + "/" + str(max_health) + " health.")


def use_potions():
    """To increase / heal health by 1 if the player has enough items"""
    global health
    global max_health
    heal_item_to_use = input("""
    Do you want to use a potion, an elixir, or continue exploring?""")
    if heal_item_to_use == "potion":
        if health < max_health and inventory["potions"] > 0:
            inventory["potions"] = inventory["potions"] - 1
            health = health + 1
            print("You healed one health!")
        elif inventory["potions"] == 0:
            print("You don't have any potions!")
        elif health == max_health:
            print("You can't heal!")
    elif heal_item_to_use == "elixir":
        if inventory["elixirs"] > 0:
            max_health = max_health + 1
            inventory["elixirs"] = inventory["elixirs"] - 1
            print("Your max health has increased by 1!")
        elif inventory["elixirs"] == 0:
            print("You don't have any elixirs!")
    elif heal_item_to_use == "explore":
        gameplay()
    else:
        print("""Invalid input!
Please type 'potion', 'elixir', or 'explore'.""")
        use_potions()


def modify_gold(amount_gold):
    """Modifies player's gold"""
    global gold
    gold = gold + amount_gold
    if amount_gold >= 1:
        print(f"""You found {amount_gold} gold!""")


def fight_goblin():
    """Fight a monster, game quits if you fail"""
    global attack
    global health
    if "Healing sword" in inventory["weapons"]:
        if health < max_health:
            health = health + 1
    goblin_health = 4 - attack
    if goblin_health <= 0:
        modify_gold(4)
        print("You defeated the goblin and earned four gold!")
    elif goblin_health > 0:
        goblin_outcome()


def goblin_outcome():
    """If the player doesn't have enough attack to defeat the goblin"""
    global gold
    goblin_health = 4 - attack
    fight_or_flight = input("""You don't have enough attack!
Do you want to flee or take damage to defeat the goblin?
(type 'flee' or 'take damage')""")
    if fight_or_flight == "flee":
        gold_stolen = random.choice(range(1, 4))
        if gold >= gold_stolen:
            gold_stolen = 0 - gold_stolen
            modify_gold(gold_stolen)
            print("The goblin stole some gold!")
        print("You ran away from the goblin!")
    elif fight_or_flight == "take damage":
        # Using your health to defeat the goblin
        global health
        health = health - goblin_health
        if health > 0:
            modify_gold(5)
            print("You defeated the goblin and earned five gold!")
            # If you try to use your health but don't have enough:
        elif health <= 0:
            print("You can't beat the goblin!")
    else:
        print("Please type 'flee' or 'take damage'.")
        goblin_outcome()


def witch():
    """Witch decreases max health by 1"""
    print(locations["Witch"])
    global max_health
    global health
    if health == max_health:
        health = health - 1
    max_health = max_health - 1
    return max_health


def print_organized(item, indenting=-5):
    """Organizing print for nested dictionaries"""
    if type(item) == dict:
        print('')
        indenting += 5
        for attributes in item:
            print(indenting * ' ', end='')
            print(attributes, end='')
            print_organized(item[attributes], indenting)
    else:
        print(item)


def buy_items():
    """Gives the player the option to purchase an item."""
    print("Market Inventory:")
    print_organized(weapon)
    print_organized(healing_stuff)
    print("")
    choice = input("Would you like to make a purchase?")
    if choice == "yes":
        global gold
        global attack
        purchase_choice = input("What would you like to purchase?")
        if purchase_choice in inventory["weapons"]:
            print("Please select a weapon we have in stock!")
            buy_items()
        if purchase_choice == "rusty knife":
            if "rusty knife" not in inventory["weapons"]:
                if gold >= 1:
                    gold = gold - 1
                    inventory["weapons"].append("rusty knife")
                    attack = attack + 1
                    del(weapon["Rusty knife"])
                    print("Thank you for your purchase!")
                elif gold < 1:
                    print("You don't have enough gold!")
        elif purchase_choice == "pocket knife":
            if "pocket knife" not in inventory["weapons"]:
                if gold >= 2:
                    gold = gold - 2
                    inventory["weapons"].append("pocket knife")
                    attack = attack + 1
                    del(weapon["Pocket knife"])
                    print("Thank you for your purchase!")
                elif gold < 2:
                    print("You don't have enough gold!")
        elif purchase_choice == "dagger":
            if "dagger" not in inventory["weapons"]:
                if gold >= 5:
                    gold = gold - 5
                    inventory["weapons"].append("dagger")
                    attack = attack + 3
                    del(weapon["Dagger"])
                    print("Thank you for your purchase!")
                elif gold < 5:
                    print("You don't have enough gold!")
        elif purchase_choice == "healing sword":
            if ("healing sword" not in inventory["weapons"]
            and "rusty knife" in inventory["weapons"]):
                if gold >= 20:
                    gold = gold - 20
                    inventory["weapons"].append("healing sword")
                    attack = attack + 5
                    del(weapon["Healing sword"])
                    inventory["weapons"].remove("rusty knife")
                    print("Thank you for your purchase!")
                elif gold < 20:
                    print("You don't have enough gold!")
            else:
                print("You can't purchase this weapon!")
        elif purchase_choice == "rusty broadsword":
            if "rusty broadsword" not in inventory["weapons"]:
                if gold >= 8:
                    gold = gold - 8
                    inventory["weapons"].append("rusty broadsword")
                    attack = attack + 2
                    del(weapon["Rusty broadsword"])
                    print("Thank you for your purchase!")
                elif gold < 5:
                    print("You don't have enough gold!")
        elif purchase_choice == "broadsword":
            if "broadsword" not in inventory["weapons"]:
                if gold >= 15:
                    gold = gold - 15
                    inventory["weapons"].append("broadsword")
                    attack = attack + 4
                    del(weapon["Broadsword"])
                    print("Thank you for your purchase!")
                elif gold < 15:
                    print("You don't have enough gold!")
        elif purchase_choice == "potion":
            if gold >= 5:
                inventory.update({"potions": inventory["potions"] + 1})
                gold = gold - 5
                print("Thank you for your purchase!")
            elif gold < 5:
                print("You don't have enough gold!")
        elif purchase_choice == "elixir":
            if gold >= 15:
                inventory.update({"elixirs": inventory["elixirs"] + 1})
                gold = gold - 15
                print("Thank you for your purchase!")
            elif gold < 15:
                print("You don't have enough gold!")
        else:
            print("I don't understand your request!")
            buy_items()
    elif choice == "no":
        print("Thank you for your time!")
    else:
        print("Not a valid answer! Please type 'yes' or 'no'.")
        buy_items()


def characters_organized(d, indent=0):
    """Organizing character lists"""
    s = ""
    for key, value in d.items():
        s += '\t' * indent + str(key)
        if isinstance(value, dict):
            characters_organized(value, indent+1)
        else:
            s += '\t' * (indent+1) + str(value) + "\n"
    return s


def new_ally():
    """A new ally will join the party (in a certain order)"""
    global attack
    global max_health
    if "Frail Woman" not in party:
        party.append("Frail Woman")
        print("A frail woman has joined your party!\n" +
              characters_organized(characters["Frail Woman"]))
        attack = attack + 2
        max_health = max_health + 2
    elif "Glogo" not in party:
        party.append("Glogo")
        print("A glogo has joined your party!\n" +
              characters_organized(characters["Glogo"]))
        attack = attack + 3
        max_health = max_health + 1
    elif "Cat" not in party:
        party.append("Cat")
        print("A cat has joined your party!\n" +
              characters_organized(characters["Cat"]))
        attack = attack + 4
    elif party == ["Yourself", "Frail Woman", "Glogo", "Cat"]:
        print("All of the characters have joined your party!")


def choose_random_location():
    """Generates a random location with a weighted random choice."""
    random_location = random.choices(list(locations),
                                     weights=[50, 20, 7, 20, 3], k=1)
    if random_location == ["Gold"]:
        modify_gold(random.choice(range(1, 4)))
    elif random_location == ["Monster"]:
        print(locations["Monster"])
        fight_goblin()
    elif random_location == ["Witch"]:
        witch()
    elif random_location == ["Market"]:
        print(locations["Market"])
        buy_items()
    elif random_location == ["New ally!"]:
        new_ally()


def gameplay():
    """Funciton that starts gameplay and inputs player choices"""
    while True:
        for choice in player_options:
            print(choice)
        player_choice = input("Which action do you wish to choose?")
        if player_choice == "1":
            choose_random_location()
        elif player_choice == "2":
            see_inventory()
        elif player_choice == "3":
            use_potions()
        elif player_choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("""Invalid input!
Please press 1 to explore, 2 to see your inventory, or 3 to quit.""")
        if health <= 0:
            print("You're out of health!")
            print("GAME OVER")
            break

gameplay()
