from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ScorpionClan, SpiritFaction
from l5r_auto.keywords import Courtier, Shugenja, Spirit
from l5r_auto.legality import IvoryEdition, ModernEdition, SamuraiEdition, TwentyFestivalsEdition
'<i>(Shugenja may attach and cast Spells.)</i><br><b>Political Interrupt, :bow::</b> Increase any Honor loss from the action by 1.'
Yogo_Honami = Personality(card_id=9491, title='Yogo Honami', force=2, chi=4, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[ScorpionClan, SpiritFaction, SpiritFaction], keywords=[Courtier, Shugenja, Spirit], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])