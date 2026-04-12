from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Cavalry, Earth, Experienced, LionsPride, Nonhuman, Paragon, Samurai, Scout, Shugenja, Tactician, Unique, Water, Zokujin
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Battle:</b> Bow or straighten a target Personality with equal or lower Chi.'
Akodo_Furu = Personality(card_id=9823, title='Akodo Furu', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=5, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 4 Attack, with +1 strength if it targeted a Spider Clan Personality. You may discard a Terrain from your hand or destroy a Terrain in play; if you did either, draw a card.'
Ikoma_Shuji = Personality(card_id=9824, title='Ikoma Shuji', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Kitsu_Kanae = Personality(card_id=9825, title='Kitsu Kanae', force=1, chi=3, personal_honor=4, gold_cost=4, honor_requirement=10, clan=[LionClan], keywords=[Cavalry, Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After Sorano enters play or overlays: Create two 2F/2C/3PH <b>Lion Clan &#149; Samurai &#149; Ancestor &#149; Spirit</b> Personalities.'
Kitsu_Sorano_Experienced = Personality(card_id=9826, title='Kitsu Sorano', force=0, chi=4, personal_honor=4, gold_cost=7, honor_requirement=6, clan=[LionClan], keywords=[Unique, Experienced('1'), Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After your Bushido Virtue action resolves, three times per turn: Give Rika +1F.'
Matsu_Rika = Personality(card_id=9827, title='Matsu Rika', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=7, clan=[LionClan], keywords=[LionsPride, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> When paying a Gold cost, destroy your target Mine or Farm: Produce Gold equal to its base Gold Cost.'
Zlkyt = Personality(card_id=9828, title='Zlkyt', force=3, chi=2, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[LionClan], keywords=[Earth, Nonhuman, Zokujin], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])