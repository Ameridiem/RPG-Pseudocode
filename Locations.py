# Catherine McLellan
# Game Locations
# CS 30
# Oct. 20, 2021
import Inventory
import random


locations = {
    "Gold": "You found some gold!",
    "Monster": "Fight a monster!",
    "Witch": "Witch steals a health!",
    "Market": "Purchase weapons or healing items!",
    "New ally!": "New character joins party!"
}


class Monster:
    def __init__(self, name, health, damage, loot):
        self.name = name
        self.health = health
        self.damage = damage
        self.loot = loot

    def __str__(self):
        return self.name

goblin = Monster("goblin", 5, 2, 5)
troll = Monster("troll", 10, 4, 10)
imp = Monster("imp", 20, 7, 15)
lesser_demon = Monster("lesser demon", 35, 7, 20)

monsters = (goblin, troll, imp, lesser_demon)


def modify_gold(amount_gold):
    """Modifies player's gold"""
    Inventory.gold = Inventory.gold + amount_gold
    if amount_gold >= 1:
        print(f"""You found {amount_gold} gold!""")


def fight_monster():
    """Fight a monster, game quits if you fail"""
    monster_to_fight = random.choice(monsters)
    print("The {} has {} health and does {} damage".format(monster_to_fight,
          monster_to_fight.health, monster_to_fight.damage))
    fight_or_flight = input("""\
Do you want to fight the {} or run away?
(type 'fight' or 'flee').""".format(monster_to_fight))
    valid_input = False
    while not valid_input:
        if fight_or_flight == 'fight':
            if "healing sword" in Inventory.weapons:
                if Inventory.health < Inventory.max_health:
                    Inventory.health = Inventory.health + 1
            monster_to_fight.health -= Inventory.attack
            Inventory.Inventory().health -= monster_to_fight.damage
            if monster_to_fight.health <= 0:
                modify_gold(monster_to_fight.loot)
                print("You defeated the {} and\
                     earned four gold!".format(monster_to_fight))
                valid_input = True
            elif monster_to_fight.health > 0:
                monster_outcome(monster_to_fight)
                valid_input = True
        elif fight_or_flight == 'flee':
            gold_stolen = random.choice(range(1, 4))
            if Inventory.gold >= gold_stolen:
                gold_stolen = 0 - gold_stolen
                modify_gold(gold_stolen)
                print("The {} stole some gold!".format(monster_to_fight))
            print("You ran away!")
            valid_input = True
        else:
            print("Invalid input!")


def monster_outcome(monster):
    """If the player doesn't have enough attack to defeat the monster"""
    valid_input = False
    fight_or_flight = input("""You don't have enough attack!
Do you want to flee or take damage to defeat the {}?
(type 'flee' or 'take damage').""".format(monster))
    while not valid_input:
        if fight_or_flight == "flee":
            gold_stolen = random.choice(range(1, 4))
            if Inventory.gold >= gold_stolen:
                gold_stolen = 0 - gold_stolen
                modify_gold(gold_stolen)
                print("The {} stole some gold!".format(monster))
            print("You ran away from the {}!".format(monster))
            valid_input = True
        elif fight_or_flight == "take damage":
            # Using your health to defeat the goblin
            Inventory.health = Inventory.health - monster.health
            if Inventory.health > 0:
                modify_gold(5)
                print("You defeated the\
                      {} and earned five gold!".format(monster))
            # If you try to use your health but don't have enough:
            elif Inventory.health <= 0:
                print("You can't beat the {}!".format(monster))
            valid_input = True
        else:
            fight_or_flight = input("Please type 'flee' or 'take damage'.")


def witch():
    """Witch decreases max health by 1"""
    print(locations["Witch"])
    if Inventory.health == Inventory.max_health:
        Inventory.health = Inventory.health - 1
    Inventory.max_health = Inventory.max_health - 1
    return Inventory.max_health


def print_market_list(item):
    """Printing market inventory"""
    item_list = []
    for item in Inventory.classes:
        try:
            if None:
                continue
            item_list = vars(item)
            print(item_list['name'].title())
            for item in item_list:
                if item == "name":
                    continue
                if item == "list_placement":
                    continue
                if item == "quantity":
                    continue
                print(f"    {item.title()}", end='')
                print(f": {item_list[item]}")
        except TypeError:
            pass


def purchase_item(item, variable):
    """If the player decides to purchase a potion or an elixir"""
    global valid_input
    valid_amount = False
    while not valid_amount:
        try:
            amount = int(input("How many?"))
        except ValueError:
            print("Please enter a number!")
        else:
            valid_amount = True
            total_price = item.price * amount
        print("That will be", total_price, "gold.")
        valid_choice = False
        while not valid_choice:
            choice = input("Would you like to make your purchase?")
            if choice == "yes":
                if Inventory.gold >= total_price:
                    variable = variable + amount
                    Inventory.gold = Inventory.gold - total_price
                    print("Thank you for your purchase!")
                    valid_choice = True
                elif Inventory.gold < total_price:
                    print("You don't have enough gold!")
                    valid_choice = True
            elif choice == "no":
                print("Thank you for your time!")
                valid_choice = True
            else:
                print("Invalid input!")
        valid_input = True
        return variable


def purchase_weapon(weapon):
    """If the player decides to purchase a weapon"""
    global valid_input
    if Inventory.gold >= weapon.price:
        Inventory.weapons.append(weapon.name)
        Inventory.gold = Inventory.gold - weapon.price
        Inventory.attack = Inventory.attack + weapon.damage
        Inventory.classes[weapon.list_placement] = None
        print("Thank you for your purchase!")
        valid_input = True
    elif Inventory.gold < weapon.price:
        print("You don't have enough gold!")


def buy_items():
    """Gives the player the option to purchase an item."""
    global valid_input
    global potions
    global elixirs
    print("Market Inventory:")
    if "rusty knife" in Inventory.weapons:
            Inventory.classes[5] = Inventory.HealingSword()
    elif "healing sword" in Inventory.weapons:
        Inventory.classes[5] = ""
    print_market_list(Inventory.classes)
    valid_input = False
    while not valid_input:
        purchase_choice = input("""What would you like to purchase?
(Type 'no' if you do not want to buy anything)""")
        if purchase_choice == "rusty knife":
            if "rusty knife" not in Inventory.weapons:
                if "healing sword" in Inventory.weapons:
                    print("Please select something we have in stock!")
                purchase_weapon(Inventory.RustyKnife())
            else:
                print("Sorry, we don't have this in stock.")
        elif purchase_choice == "pocket knife":
            purchase_weapon(Inventory.PocketKnife())
        elif purchase_choice == "dagger":
            purchase_weapon(Inventory.Dagger())
        elif purchase_choice == "healing sword":
            if ("healing sword" not in Inventory.weapons and
               "rusty knife" in Inventory.weapons):
                if Inventory.gold >= 20:
                    Inventory.gold = Inventory.gold - 20
                    Inventory.weapons.append("healing sword")
                    Inventory.attack = Inventory.attack + 6
                    Inventory.weapons.remove("rusty knife")
                    print("Thank you for your purchase!")
                    valid_input = True
                elif Inventory.gold < 20:
                    print("You don't have enough gold!")
            else:
                print("You can't purchase this weapon!")
        elif purchase_choice == "rusty broadsword":
            purchase_weapon(Inventory.RustyBroadsword())
            valid_input = True
        elif purchase_choice == "broadsword":
            purchase_weapon(Inventory.Broadsword())
        elif purchase_choice == "potion":
            Inventory.potions = purchase_item(Inventory.Potion(),
                                              Inventory.potions)
        elif purchase_choice == "elixir":
            Inventory.elixirs = purchase_item(Inventory.Elixir(),
                                              Inventory.elixirs)
        elif purchase_choice == "no":
                print("Thank you for your time!")
                valid_input = True
        else:
            print("Sorry, we don't have that item.")


def add_characters(character, indent=0):
    """Adding character to the party"""
    Inventory.attack += character["attack"]
    Inventory.max_health += character["health"]
    s = ""
    for key, value in character.items():
        if key != "description":
            continue
        s += '\t' * indent + key.title() + ": " + value
    return s


def new_ally():
    """A new ally will join the party! (In a certain order)"""
    if "Frail Woman" not in Inventory.party:
        Inventory.party.append("Frail Woman")
        print("A frail woman has joined your party!\n" +
              add_characters(vars(Inventory.FrailWoman())))
    elif "Glogo" not in Inventory.party:
        Inventory.party.append("Glogo")
        print("A glogo has joined your party!\n" +
              add_characters(vars(Inventory.Glogo())))
    elif "Cat" not in Inventory.party:
        Inventory.party.append("Cat")
        print("A cat has joined your party!\n" +
              add_characters(vars(Inventory.Cat())))
    elif Inventory.party == ["Frail Woman", "Glogo", "Cat"]:
        print("All of the characters have joined your party!")
