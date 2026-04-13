from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import BatClan, Cavalry, Elite, Gunso, Ninja, StormRider, Thunder, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"Enters play for 1 less Gold if you are a Mantis Clan player.<br><b>Reaction:</b> After another player's action targets a card in this unit, negate the action's effects on this Follower.<br><b>Battle:</b> Ranged 6 Attack."
Champion_of_Thunder = Follower(card_id=1292, title='Champion of Thunder', force=8, chi=0, personal_honor=0, gold_cost=12, focus_value=3, honor_requirement=0, keywords=[Cavalry, StormRider, Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Destroy a target enemy card without attachments.<br><b>Tireless Battle/Open:</b> Straighten this Follower's unit."
Elite_Sentry = Follower(card_id=2304, title='Elite Sentry', force=6, chi=0, personal_honor=0, gold_cost=10, focus_value=4, honor_requirement=0, keywords=[Elite, Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'You may include up to 10 copies of this card in your deck.<br>Will only attach to a Ninja.<br>After this Follower enters play, lose 1 Honor.<br><b>Ninja Battle:</b> If this Follower is in your hand, target your performing Ninja and Equip it to him.'
Fading_Shadows = Follower(card_id=2437, title='Fading Shadows', force=1, chi=0, personal_honor=0, gold_cost=0, focus_value=0, honor_requirement=0, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Enters play paying 1 less Gold if you are a Crane Clan player.<br><b>Reaction:</b> After the resolution of an action that moved a target enemy Infantry Personality to this card's battlefield: Bow the Personality."
Legion_of_the_Bat = Follower(card_id=4700, title='Legion of the Bat', force=3, chi=0, personal_honor=0, gold_cost=5, focus_value=2, honor_requirement=0, keywords=[Cavalry, BatClan], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Give each of your other Followers at the current battlefield and at each adjacent battlefield +1F.'
Moto_Gunso = Follower(card_id=5320, title='Moto Gunso', force=2, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=2, keywords=[Cavalry, Gunso], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Ranged Attacks targeting cards in this unit have -3 strength.<br><b>Political Reaction:</b> After your performing Personality enters play, if this card is in your hand or your discard pile: Attach this card to him, paying all costs. Gain 1 Honor.'
Singh_Remnants = Follower(card_id=7271, title='Singh Remnants', force=1, chi=0, personal_honor=0, gold_cost=2, focus_value=4, honor_requirement=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])