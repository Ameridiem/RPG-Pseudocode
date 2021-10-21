# Catherine McLellan
# Gameplay function
# CS 30
# Oct. 20, 2021
import Inventory
import Map
options = "1. Explore", "2. See inventory", "3. Heal", "4. See map", "5. Quit"


def gameplay():
    """Funciton that starts gameplay and inputs player choices"""
    while True:
        for choice in options:
            print(choice)
        player_choice = input("Which action do you wish to choose?")
        if player_choice == "1":
            Map.move_choice()
        elif player_choice == "2":
            Inventory.see_inventory()
        elif player_choice == "3":
            Inventory.use_potions()
        elif player_choice == "4":
            Map.update_game_map()
        elif player_choice == "5":
            print("Thanks for playing!")
            break
        else:
            print("""Invalid input!
Please press a number for your chosen action.""")
        if Inventory.health <= 0:
            print("You're out of health!")
            print("GAME OVER")
            break
