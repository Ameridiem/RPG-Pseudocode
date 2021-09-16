# RPG-Pseudocode

"""Currencies and objects:
gold (to buy or sell items)
attack (to be able to complete quests)
reputation (increases or decreases prizes)
health (to complete quests if you don't have enough attack, player starts with two health. You cannot complete a quest if you do not have enough health)
weapons (when you earn a new weapon, it adds to the total amount of attack you have)
potions (heals one health)
"""

"""You enter a small village, and a merchant wants to sell you an item. It will cost you one gold, and it doesn't look like it's in good condition.
   If the player chooses to buy the item: add rusty knife to inventory (attack: 1) (removes one gold from currency, and adds one reputation)
   If the player refuses to buy the item: the merchant looks a little disappointed but thanks you for your time.
 """
   
"""A thin woman with a wooden staff and dark cloak pproaches you, her face hidden in the shoadow of her hood. "I must ask something of you," she says. "My traveling companions betrayed me and stole a precious tome of knowledge.  It tells the legend of an ancient kingdom that ruled these lands long ago, and is the last of its kind. Could you please help me retrieve it?

  If you help the woman: you earn one reputation if you have none, or six gold if you have one reputation already. The woman joins your party. She's very frail, but she will do her best to help. Gain two health and one more attack.
  If you refuse: you lose one reputation
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
  You can buy a dagger for four gold and attack increases by three, or you can buy potions for two gold each."""
  
