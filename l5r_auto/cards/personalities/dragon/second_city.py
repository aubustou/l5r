from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Alchemist, Courtier, Duelist, Earth, EmptyHand, Fire, Gamekeeper, Justicar, Kensai, Magistrate, Monk, Mountaineer, Samurai, Shugenja, Tattooed, Unique, Yojimbo
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Reaction:</b> After Horume enters play: Choose a player. He gains or loses 1 Honor.<br><b>Reaction:</b> After a duel ends that Horume won: He boasts of his talents. Gain 1 Honor.'
Kitsuki_Horume = Personality(card_id=4412, title='Kitsuki Horume', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=10, clan=[DragonClan], keywords=[Duelist, Courtier, Gamekeeper, Justicar, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> When another player's action would target one of your Shugenja at Ezuno's location, it targets Ezuno instead, if legal."
Mirumoto_Ezuno = Personality(card_id=5086, title='Mirumoto Ezuno', force=4, chi=3, personal_honor=3, gold_cost=7, honor_requirement=3, clan=[DragonClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: If Yumaru has a Weapon, you may move her home and you may move the Personality home. Otherwise, move both of them home.'
Mirumoto_Yumaru = Personality(card_id=5181, title='Mirumoto Yumaru', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[DragonClan], keywords=[Kensai, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After the resolution of your action that bowed a Personality, target a Personality at the same location: Bow him.'
Tamori_Ruya = Personality(card_id=7789, title='Tamori Ruya', force=4, chi=5, personal_honor=4, gold_cost=9, honor_requirement=8, clan=[DragonClan], keywords=[Unique, Alchemist, Earth, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"Yayu has +2F and <b>Cavalry</b> while it is not your turn.<br><b>Battle:</b> Bow or destroy one of Yayu's Spells: He lobs an alchemical potion at the enemy. Ranged 5 Attack."
Tamori_Yayu = Personality(card_id=7806, title='Tamori Yayu', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[DragonClan], keywords=[Alchemist, Earth, Mountaineer, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After the resolution of an action that bowed a Personality at Hizumi's battlefield, target him: Negate his next straightening <i>(this turn)</i>.<br><b>Battle:</b> Give the current battlefield's province +4 or -4 strength."
Togashi_Hizumi = Personality(card_id=8521, title='Togashi Hizumi', force=6, chi=4, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Earth, EmptyHand, Monk, Tattooed], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After Meiyu enters play: Give her three +1F <b>Fire </b>tokens.'
Togashi_Meiyu = Personality(card_id=8550, title='Togashi Meiyu', force=0, chi=3, personal_honor=2, gold_cost=5, honor_requirement=4, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Fire, Monk, Tattooed], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])