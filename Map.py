# Catherine McLellan
# Map and player position
# CS 30
# Oct. 20, 2021
import Locations
import random

row = 2
column = 2
# So that the map doesn't print out when the user doesn't ask for it
print_command = 0


def update_game_map():
    """Generating and printing game map based on location_list_2"""
    global location_list2
    global print_command
    game_map = """
+--------------------------------------------------------------------------+
| {}""".format(location_list2[0][0]) + " | {}".format(location_list2[0][1]) + " | {}".format(location_list2[0][2]) + " | {}".format(location_list2[0][3]) + " | {} |".format(location_list2[0][4]) + """
+--------------------------------------------------------------------------+
| {}""".format(location_list2[1][0]) + " | {}".format(location_list2[1][1]) + " | {}".format(location_list2[1][2]) + " | {}".format(location_list2[1][3]) + " | {} |".format(location_list2[1][4]) + """
+--------------------------------------------------------------------------+
| {}""".format(location_list2[2][0]) + " | {}".format(location_list2[2][1]) + " | {}".format(location_list2[2][2]) + " | {}".format(location_list2[2][3]) + " | {} |".format(location_list2[2][4]) + """
+--------------------------------------------------------------------------+
| {}""".format(location_list2[3][0]) + " | {}".format(location_list2[3][1]) + " | {}".format(location_list2[3][2]) + " | {}".format(location_list2[3][3]) + " | {} |".format(location_list2[3][4]) + """
+--------------------------------------------------------------------------+
| {}""".format(location_list2[4][0]) + " | {}".format(location_list2[4][1]) + " | {}".format(location_list2[4][2]) + " | {}".format(location_list2[4][3]) + " | {} |".format(location_list2[4][4]) + """
+--------------------------------------------------------------------------+"""
    # The print command is only equal to 0 when the user selects action 4
    if print_command == 0:
        print(game_map)

# location_list2 will be reevaluated as this list
# There are extra spaces so the game map looks nice
location_list = [
    ["   Monster  ", "   Market   ", "    Gold    ",
        "    Witch   ", "  New ally  "],
    ["    Gold    ", "    Gold    ", "    Gold    ",
        "   Monster  ", "    Witch   "],
    ["    Gold    ", "   Monster  ", "    Start   ",
        "    Gold    ", "   Market   "],
    ["   Market   ", "    Witch   ", "    Gold    ",
        "   Monster  ", "   Monster  "],
    ["    Gold    ", "   Market   ", "    Gold    ",
        "   Monster  ", "    Gold    "]
]

# Making a list with the same values that get replaced by "You're here"
# so the "You're here" tiles don't overwrite the game map
location_list2 = [
    ["   Monster  ", "   Market   ", "    Gold    ",
        "    Witch   ", "  New ally  "],
    ["    Gold    ", "    Gold    ", "    Gold    ",
        "   Monster  ", "    Witch   "],
    ["    Gold    ", "   Monster  ", "    Start   ",
        "    Gold    ", "   Market   "],
    ["   Market   ", "    Witch   ", "    Gold    ",
        "   Monster  ", "   Monster  "],
    ["    Gold    ", "   Market   ", "    Gold    ",
        "   Monster  ", "    Gold    "]
]


def reset_location_list():
    """Resetting the "You're here" tiles to the original location_list"""
    global row
    global column
    if location_list2[row][column] == " You're here":
        location_list2[row][column] = location_list[row][column]


def player_location():
    """Calls functions based on the tile the player is located at"""
    if location_list[row][column] == "    Start   ":
        print("You are at the start. Please choose an action.")
    elif location_list[row][column] == "    Gold    ":
        Locations.modify_gold(random.choice(range(1, 4)))
    elif location_list[row][column] == "   Monster  ":
        print(Locations.locations["Monster"])
        Locations.fight_goblin()
    elif location_list[row][column] == "    Witch   ":
        Locations.witch()
    elif location_list[row][column] == "   Market   ":
        print(Locations.locations["Market"])
        Locations.buy_items()
    elif location_list[row][column] == "  New ally  ":
        Locations.new_ally()


def move_choice():
    """Changes player's position on map depending on their choice"""
    global row
    global column
    global print_command
    global location_list2
    reset_location_list()
    valid_input = False
    # Repeats loop until user puts in a valid answer
    while not valid_input:
        direction = input("Do you want to go north, south, east, or west?")
        try:
            if direction == "north":
                row = row - 1
            elif direction == "south":
                row = row + 1
            elif direction == "east":
                column = column + 1
            elif direction == "west":
                column = column - 1
            else:
                print("Invalid input!")
            if row < 0:
                row = row + 1
                raise IndexError
            elif row > 4:
                row = row - 1
                raise IndexError
            elif column < 0:
                column = column + 1
                raise IndexError
            elif column > 4:
                column = column - 1
                raise IndexError
        except IndexError:
            print("You can't go in this direction!")
        else:
            print_command = 1
            player_location()
            location_list2[row][column] = " You're here"
            update_game_map()
            print_command = 0
            valid_input = True
