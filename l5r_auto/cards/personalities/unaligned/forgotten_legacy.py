from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NagaFaction, Unaligned
from l5r_auto.keywords import Abomination, Champion, Commander, Conqueror, Naga, Nonhuman, Pearl, Shugenja, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"After The Dark Naga enters play: Lose 3 Honor.<br><b>Reaction:</b> After another player targets The Dark Naga with an action: You may bow one of your Forests. If you did, negate The Dark Naga's destruction from the action's effects.<br><b>Battle:</b> Target an enemy Personality: If he is Nonhuman, take control of him <i>(he joins your army)</i>. If he is human, bow his unit. Destroy him before this turn ends."
The_Dark_Naga = Personality(card_id=8012, title='The Dark Naga', force=9, chi=6, personal_honor=0, gold_cost=12, honor_requirement=None, clan=[Unaligned, NagaFaction], keywords=[Unique, Champion, Naga, Nonhuman, Pearl, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Enters play paying 1 less Gold for each Nonhuman you control, up to 3 less Gold.<br><b>Battle:</b> Target an enemy Personality: Bow him or move him home.'
The_Shakash = Personality(card_id=8320, title='The Shakash', force=4, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned, NagaFaction], keywords=[Conqueror, Commander, Naga, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Enters play paying 1 less Gold.<br><b>Battle:</b> Twice per turn, bow one of your Forests or Pearls: Give each of your Nonhuman cards at the current battlefield +1F.'
The_Sleepless_One = Personality(card_id=8339, title='The Sleepless One', force=4, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned, NagaFaction], keywords=[Abomination, Naga, Nonhuman, Pearl, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])