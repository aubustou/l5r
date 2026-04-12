from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Air, Cavalry, Duelist, Earth, Experienced, Goblin, Hero, Kensai, Ninja, Nonhuman, OnyxChampion, Ronin, Samurai, Scout, Shadowlands, Shugenja, Tactician, Troll, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'After Keppo enters play: Lose 2 Honor.<br><b>Battle:</b> If you have Reconnaissance, target an enemy attachment: Destroy it.'
Keppo = Personality(card_id=4328, title='Keppo', force=3, chi=2, personal_honor=0, gold_cost=3, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Goblin, Nonhuman, Scout, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Will not gain a Clan alignment.<br><b>Iaijutsu Battle:</b> Target an enemy card without attachments: Destroy it.'
Kuronada_Experienced_2 = Personality(card_id=4611, title='Kuronada', force=6, chi=5, personal_honor=3, gold_cost=10, honor_requirement=0, clan=[Unaligned], keywords=[Duelist, Experienced('2'), Kensai, Tactician, Unique, Hero, Ronin, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After Predator enters play: Lose 3 Honor.<br><b>Battle:</b> Target a Personality opposing Predator at the current battlefield: Move the Personality and Predator to the same adjacent unresolved battlefield.'
Sea_Troll_Predator = Personality(card_id=6522, title='Sea Troll Predator', force=6, chi=4, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Tactician, Earth, Nonhuman, Shadowlands, Troll], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Ranged 4 Attack.'
Shikaro = Personality(card_id=6850, title='Shikaro', force=4, chi=3, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[Unaligned], keywords=[Cavalry, Ronin, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After Takasho enters play: Lose 3 Honor.<br><b>Battle:</b> If any enemy units are at the current battlefield: Move Takasho there. You may take an additional Battle action which Takasho must perform.<br><b>Maho Battle:</b> Ranged 5 Attack.'
Takasho = Personality(card_id=7741, title='Takasho', force=3, chi=4, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[Unaligned, NinjaFaction, ShadowlandsFaction], keywords=[Unique, Air, Ninja, OnyxChampion, Shadowlands, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])