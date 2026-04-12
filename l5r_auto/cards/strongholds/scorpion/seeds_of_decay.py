from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import ScorpionClan
from l5r_auto.legality import EmperorEdition, ModernEdition
"You do not lose Honor from Ninja cards you own.<br>When another player's Battle action would target your Ninja: He is a master of the art of Ninjutsu. Once per battle, you may choose your Ninja at the same location. If you did, the action targets it instead, if legal."
The_Castle_of_Order = Stronghold(card_id=10185, title='The Castle of Order', gold_production='4', starting_family_honor=0, province_strength=7, clan=[ScorpionClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])