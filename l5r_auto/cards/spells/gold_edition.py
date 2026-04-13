from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air
from l5r_auto.legality import GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, TwentyFestivalsEdition
"After you Equip this Spell, give it a number of tokens equal to this Shugenja's Chi. <br><b>Air Limited:</b> Bow this Shugenja, and destroy a token on this Spell unless he is Scorpion Clan, to dishonor a target Personality."
Secrets_on_the_Wind = Spell(card_id=6553, title='Secrets on the Wind', gold_cost=3, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])