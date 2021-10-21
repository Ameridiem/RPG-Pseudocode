# Catherine McLellan
# Inventory and characters
# CS 30
# Oct. 20, 2021
import Locations
import Gameplay

weapon = {
    "rusty knife":
    {
        "Description: ": "A puny knife that has rusted over.",
        "Price: ": "Costs 1 gold"},
    "pocket knife":
    {
        "Description: ": "A tiny blade. Looks like a letter opener.",
        "Price: ": "Costs 2 gold"},
    "dagger":
    {
        "Description: ": "Slightly better than a pocket knife.",
        "Price: ": "Costs 5 gold"},
    "rusty broadsword":
    {
        "Description: ": "Looks really old but still has some fight left.",
        "Price: ": "Costs 8 gold"},
    "broadsword":
    {
        "Description: ": "A hero's sword.",
        "Price: ": "Costs 15 gold"}
    }

special_weapon = {
    "healing sword":
    {
        "Description: ": "Upgraded rusty knife, heals you when you fight!",
        "Price: ": "Costs 20 gold and requires the rusty knife."}}

healing_stuff = {
    "potion":
    {"Description: ": "Heals one health.",
        "Cost: ": "5 gold."},
    "elixir":
    {"Description: ": "Adds to maximum health.",
        "Cost: ": "15 gold."}
}

party = ["Yourself"]

characters = {
    "Frail Woman":
    {
        "Description: ": "She's very frail, but she will do her best to help.",
        "Stats: ": "Attack increases by 2, Max health increases by 2"},
    "Glogo":
    {
        "Description: ":
        """A squat, grey-skinned creature with round, red eyes,
and rows of spikes on its back.""",
        "Stats: ": "Attack increases by 3, Max health increases by 1"},
    "Cat":
    {
        "Description: ":
        "A massive, blue cat that looks like it wants to eat you.",
        "Stats: ": "Attack increases by 4"}
}

inventory = {"potions": 0, "elixirs": 0, "weapons": []}
health = 2
max_health = 2


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
    print("Your total attack is " + str(Locations.attack) + ".")
    print("You have " + str(Locations.gold) + " gold.")
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
        Gameplay.gameplay()
    else:
        print("""Invalid input!
Please type 'potion', 'elixir', or 'explore'.""")
        use_potions()
