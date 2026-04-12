from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import BitterLies, Courtier, Duelist, Experienced, Kensai, Loyal, Magistrate, Ninja, Paragon, Samurai, Seductress, Unique, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Battle:</b> Ranged 4 Attack. If the Ranged Attack destroyed a card, its owner loses 1 Honor.'
Bayushi_Higaonna = Personality(card_id=775, title='Bayushi Higaonna', force=5, chi=3, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br><b>Battle:</b> Bow a target enemy card without attachments. If Toshimo has a Weapon or you control a Courtier, the card cannot straighten.'
Bayushi_Toshimo = Personality(card_id=916, title='Bayushi Toshimo', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[ScorpionClan], keywords=[Kensai, Loyal, BitterLies, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, CelestialEdition, ModernEdition])
"Will not attach non-Ninja Followers.<br><b>Reaction:</b> When an action would target a Ninja at Aroru's location: Choose another of your cards. The action targets it instead, if legal. After the action's resolution, you may move Aroru to a different location.<br><b>Battle:</b> Other players may not take Reactions until this action ends. Ranged 5 Attack."
Shosuro_Aroru_Experienced_2 = Personality(card_id=7089, title='Shosuro Aroru', force=4, chi=5, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Duelist, Experienced('2'), Unique, Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Open:</b> Bow Makiko: Take the Imperial Favor.'
Shosuro_Makiko = Personality(card_id=7126, title='Shosuro Makiko', force=2, chi=4, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Courtier, Seductress], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])