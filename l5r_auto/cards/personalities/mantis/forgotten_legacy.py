from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import BountyHunter, Earth, Experienced, Magistrate, Naval, Samurai, Scout, Shugenja, Thunder, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Reaction:</b> Once per game, after Hisano enters play: Create a 2F/2C/3PH <b>Mantis Clan &#149; Nonhuman &#149; Fox &#149; Spirit &#149; Unique</b> Personality with the ability, "<b>Battle:</b> Target an enemy attacking Personality: Move him home."'
Kitsune_Hisano_Experienced = Personality(card_id=4464, title='Kitsune Hisano', force=3, chi=4, personal_honor=4, gold_cost=8, honor_requirement=2, clan=[MantisClan], keywords=[Naval, Unique, Earth, Experienced('1'), Scout, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Battle resolution does not bow cards in this unit.'
Moshi_Sasako = Personality(card_id=5279, title='Moshi Sasako', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Shugenja, Thunder], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Ranged 4 Attack. If the Ranged Attack destroyed a card, you may target and straighten a Holding.'
Tsuruchi_Nobukatsu = Personality(card_id=8861, title='Tsuruchi Nobukatsu', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[MantisClan], keywords=[BountyHunter, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Ranged 3 Attack with +2 strength if you have Reconnaissance.'
Yoritomo_Haruhiko = Personality(card_id=9556, title='Yoritomo Haruhiko', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])