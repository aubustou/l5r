from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan, NagaFaction
from l5r_auto.keywords import Artisan, Berserker, Blacksmith, Courtier, Experienced, Hero, Merchant, Naga, Samurai, Scout, Tactician, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Limited:</b> Target your Personality: Create a +1F <b>Armor</b> or <b>Weapon</b> Item and attach it to him.<br><b>Battle:</b> Target an enemy card without attachments: Bow it. If it is an attachment, remove it from the game.'
Hida_Fubatsu_Experienced = Personality(card_id=3091, title='Hida Fubatsu', force=6, chi=3, personal_honor=3, gold_cost=10, honor_requirement=3, clan=[CrabClan, NagaFaction], keywords=[Tactician, Unique, Artisan, Blacksmith, Experienced('1'), Hero, Naga, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Bow him. He may not perform actions.'
Hiruma_Nikaru = Personality(card_id=3310, title='Hiruma Nikaru', force=7, chi=2, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[CrabClan], keywords=[Berserker], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow your performing Follower: Ranged 4 Attack which may target a Personality with attached Followers if you have Reconnaissance.'
Toritaka_Chokichi = Personality(card_id=8644, title='Toritaka Chokichi', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[CrabClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Open:</b> Target another player's Personality: His controller chooses to either pay 4 Gold, lose 2 Honor, or do neither. If he did not pay 4 Gold or lose 2 Honor, the Personality may not be assigned, and will not move, into attacking armies."
Yasuki_Daiki = Personality(card_id=9436, title='Yasuki Daiki', force=2, chi=4, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])