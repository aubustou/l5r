from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan, ShadowlandsFaction
from l5r_auto.keywords import Air, BloodOfKinuye, Cavalry, Courtier, Duelist, Earth, ElementalMaster, Experienced, Fire, GoldenArm, Henshin, Inquisitor, Ishiken, LegionOfFlame, Magistrate, Monk, Samurai, Shadowlands, Shugenja, Unique, Void, Water, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Political Open:</b> Straighten a target Holding.'
Agasha_Kodo = Personality(card_id=142, title='Agasha Kodo', force=0, chi=4, personal_honor=4, gold_cost=7, honor_requirement=6, clan=[PhoenixClan], keywords=[Courtier], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Asako_Moeru = Personality(card_id=566, title='Asako Moeru', force=0, chi=3, personal_honor=3, gold_cost=4, honor_requirement=0, clan=[PhoenixClan], keywords=[Inquisitor, Ishiken, Magistrate, Shugenja, Void], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Maho Battle:</b> Target an enemy Personality: His controller may put any attachments in that unit into his hand. Give the Personality -2C.'
Asako_Rikate = Personality(card_id=576, title='Asako Rikate', force=4, chi=2, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[PhoenixClan, BrotherhoodOfShinsei, ShadowlandsFaction], keywords=[BloodOfKinuye, Earth, GoldenArm, Henshin, Monk, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Kojiro has <b>Naval</b> while he has a Spell.'
Isawa_Kojiro = Personality(card_id=3850, title='Isawa Kojiro', force=5, chi=5, personal_honor=2, gold_cost=10, honor_requirement=6, clan=[PhoenixClan], keywords=[Cavalry, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Target an Air Shugenja or a Holding: Straighten it.<br><b>Battle:</b> Target an enemy Personality: Bow him. Destroy him if he is Kolat, Ninja, or Shadowlands.'
Isawa_Mitsuko_Experienced = Personality(card_id=3866, title='Isawa Mitsuko', force=4, chi=5, personal_honor=3, gold_cost=9, honor_requirement=6, clan=[PhoenixClan], keywords=[Unique, Air, ElementalMaster, Experienced('1'), Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Iaijutsu Battle:</b> Target an enemy Personality: Kudome duels him. Bow the duel's loser. Give Kudome a +1F <b>Fire </b>token if she won and you control a Shugenja."
Shiba_Kudome = Personality(card_id=6774, title='Shiba Kudome', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=6, clan=[PhoenixClan], keywords=[Duelist, Fire, LegionOfFlame, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])