#CS 30: Continuous Game Play Assignment
#Catherine McLellan
#September 21, 2021

#Player status at the beginning of the game:
inventory = []
gold = 1
health = 2
max_health = 2
attack = 0
#Health of a monster you can fight:
goblin_health = 4
#Making a tuple of all the possible actions you can choose from:
possible_actions = ("1. See inventory", "2. Gain one gold",
"3. Heal", "4. Buy a weapon", "5. Train", "6. Fight a goblin")
#Welcoming the player and game introduction
print("""Welcome to my RPG game!
This game was inspired by the boardgame Above and Below.
Type 'quit' if you want to stop the game.""")

#Making a function that prints out your inventory and player status
def see_inventory():
	for items in inventory:
		print("You have a "+items+".")
	if inventory == []:
		print("You have no items.")
	print("Your attack is "+str(attack)+".")
	print("You have "+str(gold)+" gold.")
	print("You have "+str(health)+"/"+str(max_health)+" health.")

#Function to add one gold to your inventory
def modify_gold(amount_gold):
	global gold
	gold = gold + amount_gold

#Function to gain back your health 
def heal_health(heal_amount):
	global health
	global max_health
	if health < max_health:
		health = health + heal_amount
		print("You have "+str(health)+"/"+str(max_health)+" health.")
	else:
		print("You're at your maximum health!")

#Function that gives you the choice to purchase a rusty knife
#In the RPG game, you can't get the same kind of weapon 
# -> amount of weapons won't be an issue
def buy_a_weapon():
	choice = input("You can buy a rusty knife for 1 gold.")
	if choice == "yes":
		global gold
		if gold >= 1:
			gold = gold - 1
			inventory.append("rusty knife")
			global attack
			attack = attack +1
			print("Thank you for your purchase! Your attack has increased by 1.")
		elif gold <= 1:
			print("You don't have enough gold!")
	elif choice == "no":
		print("Thank you for your time!")
	else:
		print("Not a valid answer! Please type 'yes' or 'no'.")
		buy_a_weapon()

#Function that adds to your total attack
def train(train_amount):
	global attack
	attack = attack + train_amount
	print("You have increased your attack level to "+str(attack)+".")

#Function to fight a goblin
def fight_goblin():
	global attack
	global health
	goblin_health = 4 - attack
	if goblin_health <=0:
		print("You defeated the goblin!")
	elif goblin_health >0:
		goblin_outcome()
#If you don't have enough attack to defeat the goblin:
def goblin_outcome():
	goblin_health = 4 - attack
	fight_or_flight = input("""You don't have enough attack!
Do you want to flee or take damage to defeat the goblin?
(type 'flee' or 'take damage')""")
	if fight_or_flight == "flee":
		global gold
		if gold >=1:
			modify_gold(-1)
			print("The goblin steals one of your gold!")
		print("You ran away from the goblin!")
	elif fight_or_flight == "take damage":
		#Using your health to defeat the goblin
		global health
		health = health - goblin_health
		if health >0:
			print("You defeated the goblin!")
		#If you try to use your health but don't have enough:
		elif health <=0:
			print("You don't have enough health!")
			print("GAME OVER")
	else:
		print("Please type 'flee' or 'take damage'.")
		goblin_outcome()

#Continuous gameplay and calling defined functions based on player's choice.
while True:
	print("Type in a number to choose your action:")
	for i in possible_actions:
		print(i)
	chosen_action = input()
	if chosen_action == "quit":
		print("Thanks for playing!")
		break
	if chosen_action == "1":
		see_inventory()
	elif chosen_action == "2":
		modify_gold(1)
		print("You have a total of "+str(gold)+" gold.")
	elif chosen_action == "3":
		heal_health(1)
	elif chosen_action == "4":
		buy_a_weapon()
	elif chosen_action == "5":
		train(1)
	elif chosen_action == "6":
		fight_goblin()
		if health <=0:
			break
	else:
		print("Please type a number from 1-6 to choose an action.")