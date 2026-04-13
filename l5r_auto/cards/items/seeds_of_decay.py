from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Armor, Churetsu, Experienced, NoboriRaiu, Suryn, Unique, Weapon
from l5r_auto.legality import EmperorEdition, ModernEdition
"Negate all <i>(current and new)</i> Force and Chi penalties to this Personality from other players' actions."
Akabeko = Item(card_id=10110, title='Aka-beko', force=1, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this Personality unless he is Nonhuman: Melee Attack with strength equal to his Force.'
Blades_of_the_Black_Dragon = Item(card_id=10111, title='Blades of the Black Dragon', force=3, chi=1, gold_cost=4, focus_value=3, keywords=[Unique, Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Dragon Clan Personality.<br>This card has +1F for each Dragon Clan Personality you control.<br>After this card enters play, gain 2 Honor.<br>After this card enters play, search your discard pile, then deck, for a Ring. Show it. Put it into play or your hand. If this put it into play, while it remains in play, it does not count towards an Enlightenment Victory.'
Celestial_Sword_of_the_Dragon_Experienced = Item(card_id=10112, title='Celestial Sword of the Dragon', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), Suryn], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Mantis Clan Personality.<br>This card has +1F for each Mantis Clan Personality you control.<br>After this card enters play: Gain 2 Honor.<br><b>Battle:</b> Pay zero or more Gold: Give this Personality a Force bonus equal to the amount paid plus two, or Melee Attack with strength equal to twice the amount paid.'
Celestial_Sword_of_the_Mantis_Experienced = Item(card_id=10113, title='Celestial Sword of the Mantis', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Experienced('1'), NoboriRaiu], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Will only attach to a Scorpion Clan Personality.<br>This card has +1F for each Scorpion Clan Personality you control.<br>After this card enters play: Choose a player. He loses 2 Honor.<br><b>Battle:</b> Target an enemy card without attachments: Bow it. You may discard a card in the current battlefield's province. If you discarded a Personality or you control a Courtier, destroy the target."
Celestial_Sword_of_the_Scorpion_Experienced = Item(card_id=10114, title='Celestial Sword of the Scorpion', force=1, chi=1, gold_cost=8, focus_value=4, keywords=[Unique, Weapon, Churetsu, Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your minimum Fate deck size is decreased by one.<br>You may not choose this card to be discarded as a cost or effect of your actions if you have other cards in your hand.'
Hatogurama = Item(card_id=10115, title='Hato-gurama', force=0, chi=0, gold_cost=1, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'May attach to a Personality with exactly one Weapon.<br>After this card attaches <i>(or transfers)</i>: Dishonor this Personality unless he is Mantis Clan.<br>This Personality may attach two Weapons.'
Kama = Item(card_id=10116, title='Kama', force=3, chi=0, gold_cost=1, focus_value=1, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Effects of Political actions this Personality performs will not be negated.'
KiUso = Item(card_id=10117, title='Ki-Uso', force=0, chi=0, gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Light_Armor = Item(card_id=10118, title='Light Armor', force=3, chi=0, gold_cost=2, focus_value=3, keywords=[Armor], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Remove this card and any number of Holdings you control with total base Gold Cost of 10 or higher from the game: Gain a province to the left of your leftmost province.'
Mining_Apparatus = Item(card_id=10120, title='Mining Apparatus', force=0, chi=0, gold_cost=10, focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After an action resolves, if a player gained Honor from its effects: Give this Personality a +1F token.<br><b>Battle:</b> Target a Personality: Move him home. While this card is at the current battlefield, negate his movement to it. Lose 1 Honor.'
Moksha_Patam = Item(card_id=10121, title='Moksha Patam', force=0, chi=0, gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card and target a Nonhuman or Shadowlands Personality: Move him home.'
Okesagoma = Item(card_id=10122, title='Okesa-goma', force=0, chi=0, gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, if your Personality won it, gain 2 Honor or draw a card.<br><b>Open:</b> Put this card on top of your Fate deck: Meditation begets readiness. Straighten the Personality to whom this card was last attached.'
Sandalwood_Incense = Item(card_id=10123, title='Sandalwood Incense', force=0, chi=0, gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'This Personality has <b>Kensai</b>.<br><b>Battle:</b> Melee 4 Attack.'
Unparalleled_Sword = Item(card_id=10124, title='Unparalleled Sword', force=4, chi=1, gold_cost=7, focus_value=4, keywords=[Weapon], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])