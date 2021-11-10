# Catherine McLellan
# Inventory and characters
# CS 30
# Oct. 20, 2021
import Map

potions = 0
elixirs = 0
weapons = []
gold = 100
health = 2
max_health = 2
attack = 0


class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw weapon objects.")

    def __str__(self):
        return self.name


class RustyKnife(Weapon):
    def __init__(self):
        self.name = "rusty knife"
        self.description = "A puny knife that has rusted over."
        self.price = 1
        self.damage = 1
        self.list_placement = 0


class PocketKnife(Weapon):
    def __init__(self):
        self.name = "pocket knife"
        self.description = "A tiny blade. Looks like a letter opener."
        self.price = 2
        self.damage = 2
        self.list_placement = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "dagger"
        self.description = "Slightly better than a pocket knife."
        self.price = 5
        self.damage = 3
        self.list_placement = 2


class RustyBroadsword(Weapon):
    def __init__(self):
        self.name = "rusty broadsword"
        self.description = "Looks really old but still has some fight left."
        self.price = 8
        self.damage = 4
        self.list_placement = 3


class Broadsword(Weapon):
    def __init__(self):
        self.name = "broadsword"
        self.description = "A hero's sword."
        self.price = 15
        self.damage = 6
        self.list_placement = 4


class HealingSword(Weapon):
    def __init__(self):
        self.name = "healing sword"
        self.description = """\
Upgraded from the rusty knife. Heals you when you fight!"""
        self.price = 20
        self.damage = 6
        self.list_placement = 5


class Potion:
    def __init__(self):
        self.name = """
potion"""
        self.description = "Heals one health."
        self.price = 5
        self.quantity = potions


class Elixir:
    def __init__(self):
        self.name = "elixir"
        self.description = "Adds to your maximum health."
        self.price = 15
        self.quantity = elixirs


class Inventory:
    def __init__(self):
        self.potions = potions
        self.elixirs = elixirs
        self.weapons = weapons
        self.attack = attack
        self.gold = gold
        self.health = health
        self.max_health = max_health

classes = [RustyKnife(), PocketKnife(), Dagger(), RustyBroadsword(),
           Broadsword(),"", Potion(), Elixir()]

party = []


class Characters:
    def __init__(self):
        raise NotImplementedError("Do not create raw Character objects.")

    def __str__(self):
        return self.name


class FrailWoman(Characters):
    def __init__(self):
        self.name = "Frail Woman"
        self.description = """
        She's very frail, but she will do her best to help."""
        self.attack = 2
        self.health = 2


class Glogo(Characters):
    def __init__(self):
        self.name = "Glogo"
        self.description = """A squat, grey-skinned creature with round, red eyes,
and rows of spikes on its back."""
        self.attack = 3
        self.health = 1


class Cat(Characters):
    def __init__(self):
        self.name = "Cat"
        self.description = """
        A massive, blue cat that looks like it wants to eat you."""
        self.attack = 4
        self.health = 0


def see_inventory():
    """Displays inventory, party, and player status"""
    total_potions = f"""You have {Inventory().potions} potions and """
    total_elixirs = f"""{Inventory().elixirs} elixirs."""
    if Inventory().potions == 1:
        total_potions = f"""You have {Inventory().potions} potion and """
    if Inventory().elixirs == 1:
        total_elixirs = f"""{Inventory().elixirs} elixir."""
    print(total_potions + total_elixirs)
    if Inventory().weapons == []:
        print("""You have no weapons!""")
    for weapon in Inventory().weapons:
        print(f"""You have a {weapon}.""")
    if party == []:
        print("You're all alone...")
    else:
        print("""Allies: """ + ", ".join(map(str, party)))
    print("Your total attack is " + str(Inventory().attack) + ".")
    print("You have " + str(Inventory().gold) + " gold.")
    print("You have " + str(Inventory().health) +
          "/" + str(Inventory().max_health) + " health.")


def use_potions():
    """To increase / heal health by 1 if the player has enough items"""
    global potions
    global elixirs
    global health
    global max_health
    heal_item_to_use = input("""
    Do you want to use a potion, an elixir, or continue exploring?""")
    valid_input = False
    while not valid_input:
        if heal_item_to_use == "potion":
            if (health < max_health and potions > 0):
                potions = potions - 1
                health += 1
                print("You healed one health!")
                valid_input = True
            elif Inventory().potions == 0:
                print("You don't have any potions!")
                valid_input = True
            elif health == max_health:
                print("You can't heal, you're at max health!")
                valid_input = True
        elif heal_item_to_use == "elixir":
            if elixirs > 0:
                max_health += 1
                elixirs -= 1
                print("Your max health has increased by 1!")
                valid_input = True
            elif Inventory().elixirs == 0:
                print("You don't have any elixirs!")
                valid_input = True
        elif heal_item_to_use == "explore":
            valid_input = True
        else:
            heal_item_to_use = input("""Invalid input!
    Please type 'potion', 'elixir', or 'explore'.""")


options = "1. Explore", "2. See inventory", "3. Heal", "4. See map", "5. Quit"


def gameplay():
    """Funciton that starts gameplay and inputs player choices"""
    while True:
        for choice in options:
            print(choice)
        try:
            player_choice = float(input("Which action do you wish to choose?"))
            if player_choice == 1:
                Map.move_choice()
            elif player_choice == 2:
                see_inventory()
            elif player_choice == 3:
                Inventory().potions = use_potions()
            elif player_choice == 4:
                Map.update_game_map()
            elif player_choice == 5:
                print("Thanks for playing!")
                break
            elif player_choice > 5:
                raise ValueError
        except ValueError:
            print("""Invalid input!
Please press a number for your chosen action.""")
        if Inventory().health <= 0:
            print("You're out of health!")
            print("GAME OVER")
            break
