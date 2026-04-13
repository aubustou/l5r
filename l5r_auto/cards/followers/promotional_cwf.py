from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Nonhuman, Shadowlands, Undead
from l5r_auto.legality import ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, TwentyFestivalsEdition
'After you Equip this Follower, lose 4 Honor. After your turn begins, give this Personality a -1C Plague token. <br><b>Battle:</b> Fear 3.'
Plague_Zombies = Follower(card_id=5972, title='Plague Zombies', force=4, chi=0, gold_cost=5, focus_value=3, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, JadeEdition, ModernEdition])