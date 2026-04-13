from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Naga, Nonhuman, Orochi, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Limited:</b> Remove this card from the game: Choose a Kiho Strategy in your discard pile. Put it into your hand.'
Hunter_of_Harmony = Follower(card_id=3522, title='Hunter of Harmony', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=2, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This Personality has <b>Naval</b>.'
Scourge_of_the_Sea = Follower(card_id=6501, title='Scourge of the Sea', force=5, chi=0, personal_honor=0, gold_cost=9, focus_value=1, honor_requirement=0, keywords=[Cavalry, Nonhuman, Orochi], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Ranged 7 Attack.<br><b>Battle:</b> Even if this card is bowed, if this Personality is Nonhuman: Straighten this unit.'
The_Vengeful = Follower(card_id=8409, title='The Vengeful', force=6, chi=0, personal_honor=0, gold_cost=8, focus_value=4, honor_requirement=0, keywords=[Unique, Naga, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])