from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Air, Cavalry, Duelist, Earth, Experienced, Fenghuang, Fire, Henshin, Inquisitor, Magistrate, Monk, Nonhuman, Samurai, Shugenja, Unique, Villain, Water, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"<b>Battle/Open:</b> Target another Personality or a Follower: Give it a Force bonus or penalty equal to Heiwa's Chi."
Asako_Heiwa = Personality(card_id=537, title='Asako Heiwa', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=6, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Earth, Henshin, Monk], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After Izuna enters play, target another player's Personality with Personal Honor lower than or equal to Izuna's Chi: She coerces testimony of a family's secret. Dishonor the targeted Personality and permanently give him <b>Kolat, Ninja, </b>or<b> Shadowlands</b>."
Asako_Izuna = Personality(card_id=546, title='Asako Izuna', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Air, Inquisitor, Magistrate, Shugenja, Villain], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After a Ranged Attack is targeted: Give the Ranged Attack +2 strength.<br><b>Battle:</b> Any number of times per turn: Ranged 1 Attack.'
Isawa_Kaname = Personality(card_id=3844, title='Isawa Kaname', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=5, clan=[PhoenixClan], keywords=[Fire, Shugenja, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets one of your other Personalities at Sakonoko's location, bow Sakonoko or one of his Spells: Negate the destruction of the Personality from the action's effects."
Isawa_Sakonoko = Personality(card_id=3891, title='Isawa Sakonoko', force=0, chi=4, personal_honor=4, gold_cost=7, honor_requirement=5, clan=[PhoenixClan], keywords=[Unique, Inquisitor, Magistrate, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Target a Personality: Give him +2F.'
Kunji = Personality(card_id=4604, title='Kunji', force=3, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[PhoenixClan], keywords=[Cavalry, Fenghuang, Nonhuman, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Even if Jouta is dead, choose your performing Shugenja, who may be at any location unless Jouta is dead: Ranged 5 Attack.'
Shiba_Jouta_Experienced = Personality(card_id=6766, title='Shiba Jouta', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=5, clan=[PhoenixClan], keywords=[Unique, Experienced('1'), Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target your Personality: Move him home. If he moved, straighten him.'
Shiba_Ryuba = Personality(card_id=6799, title='Shiba Ryuba', force=4, chi=3, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[PhoenixClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])