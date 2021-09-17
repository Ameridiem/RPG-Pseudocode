# RPG-Pseudocode - Inspired by the Game Above and Below
#Rewards and payments may or may not change depending on the difficulty of the game

"""Currencies and objects:
You lose the game if you are out of health
gold (to buy or sell items)
attack (to be able to complete quests)
weapons: rusty knife, pocket knife, dagger, broadsword, healing sword
reputation (increases or decreases prizes)
health (to complete quests if you don't have enough attack, player starts with two health. You cannot complete a quest if you do not have enough health)
weapons (when you earn a new weapon, it adds to the total amount of attack you have)
potions (heals one health)
elixir (increases max health by 1)
"""


"""A thin woman with a wooden staff and dark cloak approaches you, her face hidden in the shoadow of her hood. "I must ask something of you," she says. "My traveling companions betrayed me and stole a precious tome of knowledge.  It tells the legend of an ancient kingdom that ruled these lands long ago, and is the last of its kind. Could you please help me retrieve it?

  If you help the woman: you earn one reputation if you have none, or six gold if you have one reputation already. The woman joins your party. She's very frail, but she will do her best to help. Gain two health and two more attack.
  If you refuse: you lose one reputation
"""
  
"""You enter a small village, and a merchant wants to sell you an item. It will cost you one gold, and it doesn't look like it's in good condition.
   If the player chooses to buy the item: add rusty knife to inventory (attack: 1) (removes one gold from currency, and adds one reputation)
   If the player refuses to buy the item: the merchant looks a little disappointed but thanks you for your time.
"""
 
"""On your way, you must cross a smooth, clear river. You decide to board and see what you can find further downstream. You pass forests of huge mushrooms, bats hanging in silent swarms in tall chambers, and even a few outposts along the rocky bank. As you turn into a new passage, the water grows trough. Sharp, deadly rocks jut up in every direction, threatening to cut your little boat to pieces. There's a sandy shore on your right.
  If you stop the boat and explore: A potion if you have less than one reputation, a potion and two gold if you have one reputation.
  If you brave the rapids: You lose one health, but gain six gold and a reputation.

"""You venture into a massive cavern filled with the ruins of a crumbling city. As you wander among the cracked stone walls you smell burning wood, and soon come upon a campfire, a cloaked traveler sitting behind it. "I've explored every inch of this city, and you'll find nothing here. But, for a price, perhaps I could be persuaded to part with my knowledge of this place." For all you know, he may have just arrived.
  If you convince the man to tell you about the city: lose one gold and gain one reputation, or lose two gold and gain two reputation. The man tells you that he saw a group of three people pass by here. It seems you are on the right track.
  If you explore the city yourself: you find one potion, nothing much else around here.
"""

"""Your party finds a tent set up underneath a massive face cut into the cave rock. The embers of a campfire still glow, and you assume the woner of the tent is nearby. It might be the betrayers of the frail woman, but instead it is a squat, grey-skinned creature with round, red eyes and rows of spikes on its pack - it's a glogo.
  Loot his tent before he gets back: -2 reputation, three gold, one pocket knife (attack +1, total attack: 2)
  Befriend the glogo: Glogo joins the party, max health +1 and attack +3
"""

"""You stop at a trading post. Bright lanterns hang on the dock, and little boats fastened with thick rope bob up and down in the water.
  You can buy a dagger for four gold and attack increases by three, or you can buy potions for two gold each.

--> If the frail woman hasn't joined your party: You see the same frail woman again, she smiles, and you end up feeling really sorry for her. You agree to help her find her tomb of knowledge, even though you seem like it's a waste of time.
  """
  
"""Your party travels through a cave filled with blue crystals and soon you come upon a fishfolk woman. "Can you help me find mushrooms?" she asks. "My village is running out of food and we need help." Do you help her find mushrooms or ignore her and continue exploring?
   Search for mushrooms: you earn one reputation, you can lose one health and gain two reputation and two gold.
   Continue exploring: you lose one reputation if you have attack 3, or you lose one reputation and get five gold if you have attack 6.
"""

"""You come across a traveling merchant dressed in yellow and reining in an old, green-skinned pack-lizard. "Come, take a look at my wares," says teh merchant as shafts of daylight slice through the ceiling and light up his veiled face. The man is traveling alone, and as far as you can tell, he is unarmed. You could probably snatch one of his bags and run before he would be able to stop you. Do you haggle with the man, or steal from him?
   Haggle: You can buy a potion for 1 gold, an elixir for five gold, or a broadsword for 10 gold (attack +5)
   Steal from the merchant: requires reputation -4 and you lose three reputation, gain seven coins, and gain three potions.
"""

"""You turn a corner and come across a hug pile of bones. Moments later, a massive, blue cat emerges from the darkness. The cat's eyes are thin slits of purple, its striped, bushy tail swaying back and forth. "Find us some fish," says the cat, eyeing you hungrily. Do you fight the cat, hide from it, or search for some fish to give it?
   Hide: you lose one reputation
   Search for some fish for the cat: the cat joins your party, and your attack increases by 4.
   Fight the cat: requires attack 6, you lose two reputation and gain five gold
"""

"""Your party follows a wide passage lined with old columns until you come upon a cave filled with bright tents of red and yellow. Tall torches and lanterns light up what seems to be an underground market. As you peruse the wares offered by creatures of every shape and size, a red-bearded man leaning on a gnarled staff approaches you. "I have a proposition that will be well worth your time, if you'd care to listen," he says. Do you listen to him or haggle with the merchants?
   Haggle: Requires reputation 4, and you can pay twenty gold and gain a healing sword. Attack +5 and you gain back a health every time you fight.
   Listen to the man's proposition:
"I can tell you more when we reach my camp," says the bearded man. he beckons you to follow and leads you away from the circle of merchant tents, down a few dark passages, stopping in a round cave. You don't see any sign of his camp. Suddenly, five men emerge from the shadows, armed with heavy clubs and rocks. "My proposition is this," says the man with a wicked grin. Empty your pockets and we on't hurt you." Do you pay the thugs or fight them?
   Pay: -1 reputation, -10 gold, you may lose a weapon or two if you don't have enough gold, or you lose your health if you don't have enough weapons.
      (one weapon would be sold for half it's value, rounded down, and a health would get you one gold. If you don't have enough health, you lose the game.)
   Fight: If you have attack 5 - 2 coins, +1 reputation. If you have attack 10: 4 coins, +2 reputation
"""
   
"""After crawling up to the side of a steep cliff, your party sees two men running in the distance. "Those were my traveling companions!" yells the woman. It doesn't seem likely you'll catch up to them.
   Attempt to chase them: requires attack 7, you aren't able to catch them, but they did drop a bag containing ten gold and one potion.
   Explore the area to find a shortcut: There are no shortcuts, but you can still see those two men running away. You find a rusty broadsword (attack +3) and an elixir.
"""

"""Attempting to follow the woman's betrayers, you arrive at apassage blocked by a huge scorpion. Behind the scorpion, you can still see them running. How the heck did they get past this thing?"""
   Fight the scorpion: Attack 15, gain one reputation
   Attempt to flee the scorpion: Lose three health
"""

"""You catch up to the two men and corner them. The frail woman in your party looks very distraught. "They may look like my old traveling companions, but they don't feel like them..." They seem very apologetic and return the tome of knowledge, but in return you must cut away these strange looking bracelets. You are confused by the trade, but you make it anyways. The two men laugh wickedly and transform into a dark, shadowy demon with flaming eyes. "I'm finally free after hundreds of years! Thank you, foolish creatures. Now I will destroy you," shrieks the creature. You must fight the demon, and it requires attack 20.

You defeat the demon, and it shrieks while disappearing into a cloud of smoke. The frail woman has tears running down her eyes, and explains that she must have lost her two traveling companions long before they stole the tome of knowledge. 
