from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Castle, Experienced
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Siege Battle:</b> Bow your target Castle or Siege card: Ranged 5 Attack. If this targeted a card, gain 2 Honor.'
Carpenter_Castle = Stronghold(card_id=1218, title='Carpenter Castle', gold_production='4', starting_family_honor=4, province_strength=9, clan=[CrabClan], keywords=[Castle], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's Battle action targets your Berserker: Delay its effects on him until after this battle ends."
Halls_of_the_Forgotten = Stronghold(card_id=2950, title='Halls of the Forgotten', gold_production='4', starting_family_honor=3, province_strength=8, clan=[CrabClan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Recon Reaction:</b> After engaging: You have Reconnaissance at the current battlefield. Create and attach a 0F <B>Scout</B> Follower to each of one to three of your Personalities in your current army. Remove those Followers from the game after the battle ends.'
Kyuden_Hida_Experienced = Stronghold(card_id=4638, title='Kyuden Hida', gold_production='4', starting_family_honor=3, province_strength=8, clan=[CrabClan], keywords=[Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This Stronghold produces 1 less Gold when paying for a Personality.<br><b>Absent Tireless Battle, :g3::</b> Move home a target attacking Personality. If he moves, his controller loses 1 Honor.'
Yasuki_Palaces_Experienced = Stronghold(card_id=9459, title='Yasuki Palaces', gold_production='5', starting_family_honor=3, province_strength=7, clan=[CrabClan], keywords=[Experienced('1')], traits=[], abilities=[], legality=[EmperorEdition])