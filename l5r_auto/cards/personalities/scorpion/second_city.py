from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Actor, Air, Artisan, BitterLies, Courtier, Experienced, EyeOfShadow, FinalStudent, Kensai, Loyal, Magistrate, Ninja, Paragon, Prodigy, Samurai, Shadowspawn, Shugenja, Unique, WardMaster, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'Ranged Attacks from actions performed by Kahoku may target dishonorable Personalities with attached Followers.<br><b>Battle:</b> Target an enemy Personality: Give him -4F. Ranged 3 Attack.'
Bayushi_Kahoku_Experienced = Personality(card_id=807, title='Bayushi Kahoku', force=5, chi=4, personal_honor=1, gold_cost=9, honor_requirement=None, clan=[ScorpionClan], keywords=[Unique, Experienced('1'), FinalStudent, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Bow the Personality or all of his attachments. If he is dishonorable, his controller loses 2 Honor.'
Bayushi_Nori = Personality(card_id=857, title='Bayushi Nori', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=1, clan=[ScorpionClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Even if Hawado is bowed, remove a Dynasty card in any discard pile from the game: Move Hawado home or to a battlefield with one or more enemy units. If she moved, straighten her.'
Shosuro_Hawado = Personality(card_id=7103, title='Shosuro Hawado', force=4, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja, Shadowspawn], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Open:</b> Bow Rin and target an honorable Personality: Rin shames him in a performance. The Personality's controller may dishonor him. If he did not choose this, bow him and negate his straightening <i>(this turn)</i>."
Shosuro_Rin = Personality(card_id=7151, title='Shosuro Rin', force=2, chi=3, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[ScorpionClan], keywords=[Actor, Artisan, Courtier, EyeOfShadow], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card: Bow it. Destroy it if it has no attachments and you control a Courtier.'
Shosuro_Ritoru = Personality(card_id=7153, title='Shosuro Ritoru', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Kensai, Loyal, BitterLies, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'You may equip Air Spells to Neiru as an <b>Open</b> action.'
Soshi_Neiru = Personality(card_id=7360, title='Soshi Neiru', force=1, chi=3, personal_honor=2, gold_cost=4, honor_requirement=1, clan=[ScorpionClan], keywords=[Air, Prodigy, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Open:</b> Target another player's Personality: If he is dishonorable, his controller loses 1 Honor. Otherwise, give your provinces +2 strength."
Yogo_Adi = Personality(card_id=9485, title='Yogo Adi', force=2, chi=5, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Air, Courtier, Shugenja, WardMaster], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])