from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Air, Courtier, Duelist, Earth, Experienced, Kensai, Magistrate, Monk, Samurai, Shugenja, Tattooed, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Open:</b> Target an attachment: Bow it.'
Kitsuki_Nubane = Personality(card_id=4429, title='Kitsuki Nubane', force=3, chi=5, personal_honor=4, gold_cost=7, honor_requirement=5, clan=[DragonClan], keywords=[Duelist, Courtier, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Bow Kojinrue or one of his Weapons, and target an enemy card without attachments: Destroy it.'
Mirumoto_Kojinrue = Personality(card_id=5123, title='Mirumoto Kojinrue', force=5, chi=4, personal_honor=2, gold_cost=9, honor_requirement=4, clan=[DragonClan], keywords=[Kensai, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Kazushige has +2F while defending.<br><b>Open:</b> If it is another player's turn, target one of his Personalities: Before this phase ends, straighten him. Before this turn ends, if the Personality did not assign to attack this turn, gain 2 Honor."
Tamori_Kazushige = Personality(card_id=7777, title='Tamori Kazushige', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=0, clan=[DragonClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle/Open:</b> Even if Osawa is bowed, target a Personality at Osawa's location: Bow or straighten him."
Togashi_Osawa_Experienced = Personality(card_id=8565, title='Togashi Osawa', force=5, chi=4, personal_honor=2, gold_cost=9, honor_requirement=1, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Unique, Air, Experienced('1'), Monk, Tattooed], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])