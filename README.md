# RPG-Pseudocode - Inspired by the Game Above and Below
#Rewards, payments, and end-game points may or may not change depending on the difficulty of the game

"""Currencies and objects:
You lose the game if you are out of health
Gold (to buy or sell items, you start the game with one gold in your inventory.)
Attack (to be able to complete quests)
Weapons: rusty knife, pocket knife, dagger, broadsword, rusty broadsword, healing sword (when you earn a new weapon, it adds to the total amount of attack you have)
Reputation (increases or decreases prizes)
Health (to complete quests if you don't have enough attack, player starts with two health. You cannot complete a quest if you do not have enough health)
Potions (heals one health)
Elixir (increases max health by 1)
"""

"""When you fail the game: goes to a menu disaplaying, "Game Over" with a restart option."""


"""A thin woman with a wooden staff and dark cloak approaches you, her face hidden in the shoadow of her hood. "I must ask something of you," she says. "My traveling companions betrayed me and stole a precious tome of knowledge.  It tells the legend of an ancient kingdom that ruled these lands long ago, and is the last of its kind. Could you please help me retrieve it?"

  If you help the woman: you earn one reputation. The woman joins your party. She's very frail, but she will do her best to help. Gain two health, two more attack, and four gold
  If you refuse: you lose one reputation
"""
  
"""You enter a small village, and a merchant wants to sell you an item. It will cost you one gold, and it doesn't look like it's in good condition. He tells you it would do you good in the long run, but it looks like an old letter-opener...
   If the player chooses to buy the item: gain a reputation and a rusty knife to inventory (attack: 1) (removes one gold from currency)
   If the player refuses to buy the item: the merchant looks a little disappointed but thanks you for your time.
"""
 
"""On your way, you must cross a smooth, clear river. You decide to board and see what you can find further downstream. You pass forests of huge mushrooms, bats hanging in silent swarms in tall chambers, and even a few outposts along the rocky bank. As you turn into a new passage, the water grows rough. Sharp, deadly rocks jut up in every direction, threatening to cut your little boat to pieces. There's a sandy shore on your right.
  If you stop the boat and explore: A potion if you have less than one reputation, a potion and two gold if you have one reputation.
  If you brave the rapids: You lose two health, but gain six gold and a reputation.

"""You venture into a massive cavern filled with the ruins of a crumbling city. As you wander among the cracked stone walls you smell burning wood, and soon come upon a campfire, a cloaked traveler sitting behind it. "I've explored every inch of this city, and you'll find nothing here. But, for a price, perhaps I could be persuaded to part with my knowledge of this place." For all you know, he may have just arrived.
  If you convince the man to tell you about the city: pay one gold and gain one reputation, or pay two gold and gain two reputation. The man tells you that there is great evil nearby, and that you should be careful. You are confused by his words, since there is nothing nearby, but it doesn't hurt to be extra cautious.
  If you explore the city yourself: you find one potion, nothing much else around here.
"""

"""Your party finds a tent set up underneath a massive face cut into the cave rock. The embers of a campfire still glow, and you assume the owner of the tent is nearby. It might be one of the betrayers the frail woman mentioned, but it is a squat, grey-skinned creature with round, red eyes and rows of spikes on its pack - it's a glogo.
  Loot his tent before he gets back: -2 reputation, three gold, one pocket knife (attack +1)
  Befriend the glogo: Glogo joins the party, max health +1 and attack +3
"""

"""You stop at a trading post. Bright lanterns hang on the dock, and little boats fastened with thick rope bob up and down in the water.
  You can buy a dagger for four gold and attack increases by three, or you can buy potions for two gold each.

--> If the frail woman hasn't joined your party: You see the same frail woman again, she smiles, and you end up feeling really sorry for her. You agree to help her find her tomb of knowledge, even though you seem like it's a waste of time.
  """
  
"""Your party travels through a swamp and soon you come upon a fishfolk woman. "Can you help me find mushrooms?" she asks. "My village is running out of food and we need help." Do you help her find mushrooms or ignore her and continue exploring?
   Search for mushrooms: you earn one reputation and 5 gold, you can lose one health and gain two reputation and ten gold.
   Continue exploring: you lose one reputation and one health if you have attack 3, or you lose one reputation and health but gain 5 gold if you have attack 6.
"""

"""You turn a corner and come across a hug pile of bones. Moments later, a massive, blue cat emerges from the darkness. The cat's eyes are thin slits of purple, its striped, bushy tail swaying back and forth. "Find us some fish," says the cat, eyeing you hungrily. Do you fight the cat, hide from it, or search for some fish to give it?
   Hide: you lose one reputation
   Search for some fish for the cat: the cat joins your party, and your attack increases by 4.
   Fight the cat: requires attack 6, you lose two reputation and gain five gold
"""

"""Your party follows a wide passage into a valley when you come upon many bright tents of red and yellow. Tall torches and lanterns light up what seems to be a market. As you peruse the wares offered by creatures of every shape and size, a red-bearded man leaning on a gnarled staff approaches you. "I have a proposition that will be well worth your time, if you'd care to listen," he says. Do you listen to him or haggle with the merchants?
   Haggle: Requires reputation 2, and you can pay twenty gold if you have the rusty knife and gain a healing sword. Attack +5 and you gain back a health every time you fight. Otherwise, you can buy potions for 2 gold or an elixir for 5 gold.
   Listen to the man's proposition:
"I can tell you more when we reach my camp," says the bearded man. He beckons you to follow and leads you away from the circle of merchant tents, down a few dark passages, stopping in a round cave. You don't see any sign of his camp. Suddenly, five men emerge from the shadows, armed with heavy clubs and rocks. "My proposition is this," says the man with a wicked grin. Empty your pockets and we won't hurt you." Do you pay the thugs or fight them?
   Pay: -1 reputation, -10 gold, you may lose a weapon or two if you don't have enough gold, or you lose your health if you don't have enough weapons.
      (one weapon would be sold for half it's value, rounded down, and a health would get you one gold. If you don't have enough health, you lose the game.)
   Fight: If you have attack 5: 2 coins, +1 reputation. If you have attack 10: 4 coins, +2 reputation
"""
   
"""After crawling up to the side of a steep cliff, your party sees two men running in the distance. "Those were my traveling companions!" yells the woman. It doesn't seem likely you'll catch up to them.
   Attempt to chase them: requires attack 7, you aren't able to catch them, but they did drop a bag containing ten gold and one potion.
   Explore the area to find a shortcut: There are no shortcuts, but you can still see those two men running away. You find a rusty broadsword (attack +3) and an elixir.
"""

"""You come across a traveling merchant dressed in yellow and reining in an old, green-skinned pack-lizard. "Come, take a look at my wares," says the merchant as shafts of daylight slice through the ceiling and light up his veiled face. The man is traveling alone, and as far as you can tell, he is unarmed. You could probably snatch one of his bags and run before he would be able to stop you. Do you haggle with the man, or steal from him?
   Haggle: You can buy a potion for 1 gold, an elixir for five gold, or a broadsword for 10 gold (attack +5)
   Steal from the merchant: requires reputation below zero and you lose three reputation, gain seven coins, and gain three potions.
"""

"""Attempting to follow the woman's betrayers, you arrive at apassage blocked by a huge scorpion. Behind the scorpion, you can still see them running. How the heck did they get past this thing?"""
   Fight the scorpion: Attack 15, gain one reputation
   Attempt to flee the scorpion: Lose three health
"""

"""You catch up to the two men and corner them. The frail woman smiles warmly. "Thank you for retrieving my ancient tome..." She laughs wickedly and transform into a dark, shadowy demon with flaming eyes. "I'm finally free after hundreds of years! Thank you, foolish creatures. Now I will destroy you," shrieks the demon. You must fight the demon, and it requires attack 20. (Frail woman leaves your party and you lose 2 health and 2 attack if she joined at the beginning of the game -> may have to change this mechanic if the coding is too difficult.)

If you succeed:
You defeat the demon, and it shrieks while disappearing into a cloud of smoke. At least the frail woman wasn't lying about the tome. You use the tome to find the ruins of a great civilization, and hopfully one day, it can be habitable once again.
"""

"""END GAME POINTS:
Max health - one point each
Weapons - rusty knife (1 point) , pocket knife (1 point), dagger (2 points), broadsword (3 points), rusty broadsword (2 points), healing sword (5 points)
Healing items - elixir (1 point)
Reputation - -2 points if you have less that -3 reputation, or 2 points if you have more than 3 reputation
Gold - 1 point for every 5 gold

If the player has more than 25 points, gets a secret ending:
You help rebuild the ancient civilization, and there are remenants of ancient technology used to repel monsters and evil. Hopefully one day, you can use this to make the world a better and safer place.
"""
