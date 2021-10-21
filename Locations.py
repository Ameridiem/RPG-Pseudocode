# Catherine McLellan
# Game Locations
# CS 30
# Oct. 20, 2021
import Inventory
import random

gold = 0
attack = 0

locations = {
    "Gold": "You found some gold!",
    "Monster": "Fight a goblin!",
    "Witch": "Witch steals a health!",
    "Market": "Purchase weapons or healing items!",
    "New ally!": "New character joins party!"
}


def modify_gold(amount_gold):
    """Modifies player's gold"""
    global gold
    gold = gold + amount_gold
    if amount_gold >= 1:
        print(f"""You found {amount_gold} gold!""")


def fight_goblin():
    """Fight a monster, game quits if you fail"""
    global attack
    if "healing sword" in Inventory.inventory["weapons"]:
        if Inventory.health < Inventory.max_health:
            Inventory.health = Inventory.health + 1
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
        Inventory.health = Inventory.health - goblin_health
        if Inventory.health > 0:
            modify_gold(5)
            print("You defeated the goblin and earned five gold!")
            # If you try to use your health but don't have enough:
        elif Inventory.health <= 0:
            print("You can't beat the goblin!")
    else:
        print("Please type 'flee' or 'take damage'.")
        goblin_outcome()


def witch():
    """Witch decreases max health by 1"""
    print(locations["Witch"])
    if Inventory.health == Inventory.max_health:
        Inventory.health = Inventory.health - 1
    Inventory.max_health = Inventory.max_health - 1
    return Inventory.max_health


def print_organized(item, indenting=-5):
    """Organizing print for nested dictionaries"""
    if type(item) == dict:
        print('')
        indenting += 5
        for attributes in item:
            print(indenting * ' ', end='')
            print(attributes.title(), end='')
            print_organized(item[attributes], indenting)
    else:
        print(item)


def purchase_item(item, cost):
    """If the player decides to purchase a potion or an elixir"""
    global gold
    if gold >= cost:
        Inventory.inventory.update({item: Inventory.inventory[item] + 1})
        gold = gold - cost
        print("Thank you for your purchase!")
    elif gold < cost:
        print("You don't have enough gold!")
        buy_items()


def purchase_weapon(weapon, cost, attack_stat):
    """If the player decides to purchase a weapon"""
    global gold
    global attack
    if gold >= cost:
        Inventory.inventory["weapons"].append(weapon)
        gold = gold - cost
        attack = attack + attack_stat
        del(Inventory.weapon[weapon])
        print("Thank you for your purchase!")
    elif gold < cost:
        print("You don't have enough gold!")


def buy_items():
    """Gives the player the option to purchase an item."""
    print("Market Inventory:")
    if ("rusty knife" not in Inventory.weapon and "healing sword"
       not in Inventory.inventory["weapons"]):
        Inventory.weapon.update(Inventory.special_weapon)
    print_organized(Inventory.weapon)
    print_organized(Inventory.healing_stuff)
    print("")
    choice = input("Would you like to make a purchase?")
    if choice == "yes":
        global gold
        global attack
        purchase_choice = input("What would you like to purchase?")
        if purchase_choice not in Inventory.weapon:
            print("Please select a weapon we have in stock!")
            buy_items()
        if purchase_choice == "rusty knife":
            if "rusty knife" not in Inventory.inventory["weapons"]:
                if "healing sword" in Inventory.inventory["weapons"]:
                    print("Please select something we have in stock!")
                    buy_items()
                purchase_weapon("rusty knife", 1, 1)
        elif purchase_choice == "pocket knife":
            purchase_weapon("pocket knife", 2, 2)
        elif purchase_choice == "dagger":
            purchase_weapon("dagger", 5, 3)
        elif purchase_choice == "healing sword":
            if ("healing sword" not in Inventory.inventory["weapons"] and
               "rusty knife" in Inventory.inventory["weapons"]):
                if gold >= 20:
                    gold = gold - 20
                    Inventory.inventory["weapons"].append("healing sword")
                    attack = attack + 6
                    Inventory.inventory["weapons"].remove("rusty knife")
                    Inventory.weapon.pop("Healing sword")
                    print("Thank you for your purchase!")
                elif gold < 20:
                    print("You don't have enough gold!")
            else:
                print("You can't purchase this weapon!")
        elif purchase_choice == "rusty broadsword":
            purchase_weapon("rusty broadsword", 8, 4)
        elif purchase_choice == "broadsword":
            purchase_weapon("broadsword", 15, 4)
        elif purchase_choice == "potion":
            purchase_item("potions", 5)
        elif purchase_choice == "elixirs":
            purchase_item("elixirs", 15)
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
    """A new ally will join the party! (In a certain order)"""
    global attack
    if "Frail Woman" not in Inventory.party:
        Inventory.party.append("Frail Woman")
        print("A frail woman has joined your party!\n" +
              characters_organized(Inventory.characters["Frail Woman"]))
        attack = attack + 2
        Inventory.max_health = Inventory.max_health + 2
    elif "Glogo" not in Inventory.party:
        Inventory.party.append("Glogo")
        print("A glogo has joined your party!\n" +
              characters_organized(Inventory.characters["Glogo"]))
        attack = attack + 3
        Inventory.max_health = Inventory.max_health + 1
    elif "Cat" not in Inventory.party:
        Inventory.party.append("Cat")
        print("A cat has joined your party!\n" +
              characters_organized(Inventory.characters["Cat"]))
        attack = attack + 4
    elif Inventory.party == ["Yourself", "Frail Woman", "Glogo", "Cat"]:
        print("All of the characters have joined your party!")
