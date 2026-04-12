from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import SpiderClan
from l5r_auto.keywords import Dojo
from l5r_auto.legality import EmperorEdition, ModernEdition
'You do not lose Honor from Spider Clan and Fate cards you own. You ignore Honor Requirements on your Followers.<br><b>Battle:</b> Choose your performing Commander: If any enemy units are at the current battlefield or he assigned there, move him there. Straighten his unit if he moved.'
Keep_of_the_Dead = Stronghold(card_id=4310, title='Keep of the Dead', gold_production='4', starting_family_honor=0, province_strength=7, clan=[SpiderClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'You do not lose Honor from Spider Clan and Fate cards you own.<br>After the resolution of the first Dark Virtue action you took each phase: Draw a card.'
Steel_Soul_Dojo = Stronghold(card_id=7484, title='Steel Soul Dojo', gold_production='4', starting_family_honor=0, province_strength=7, clan=[SpiderClan], keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'You do not lose Honor from Ninja and Fate cards you own.<br><b>Ninja Battle:</b> Once per battle, even if this card is bowed and even if you control no units at the current battlefield, target one or more unopposed units with combined total Force of 9 or lower, or one opposed unit: Move each target home; this will not be negated or delayed if you control a Ninja.'
The_Shadows_Lair = Stronghold(card_id=8316, title="The Shadow's Lair", gold_production='4', starting_family_honor=0, province_strength=0, clan=[SpiderClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After your Personality enters play: You may attach a Weapon to him from your hand, paying all costs but, once per turn, paying 4 less Gold if he is a Kensai.'
The_Spiders_Web = Stronghold(card_id=8352, title="The Spider's Web", gold_production='4', starting_family_honor=1, province_strength=7, clan=[SpiderClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])