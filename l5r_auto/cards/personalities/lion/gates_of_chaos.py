from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Cavalry, ClanChampion, Conqueror, Destined, Experienced, Fallen, Hero, Loyal, Paragon, Samurai, Scout, Shugenja, SteelLion, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>Battle:</b> Bow a target enemy Personality with lower Personal Honor. Destroy him if he is Unaligned.'
Akodo_Dairuko_Experienced = Personality(card_id=10635, title='Akodo Dairuko', force=5, chi=5, personal_honor=5, gold_cost=14, honor_requirement=12, clan=[LionClan], keywords=[Conqueror, Loyal, Tactician, Unique, ClanChampion, Experienced('1'), Paragon, Samurai, SteelLion], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 3 Attack, or Ranged 4 Attack if the target is Lion Clan or Unaligned.'
Akodo_Kamina_Experienced = Personality(card_id=10636, title='Akodo Kamina', force=4, chi=4, personal_honor=3, gold_cost=11, honor_requirement=10, clan=[LionClan], keywords=[Tactician, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Nojima enters play, lose 1 Honor.<br>Destroy Nojima if he is ever in an army with a Personality with 3 or more Personal Honor.'
Akodo_Nojima = Personality(card_id=10637, title='Akodo Nojima', force=3, chi=2, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[LionClan], keywords=[Cavalry, Fallen, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"Will not gain Fallen or Shadowlands.<br>Ayumu's rulebook Tactical Advantage ability is a <b>Battle/Open</b> action for Ayumu."
Ikoma_Ayumu_Experienced = Personality(card_id=10638, title='Ikoma Ayumu', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Unique, Experienced('1'), Hero, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g1:: Refill the Province Jeiku entered play from face-up. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Ikoma_Jeiku = Personality(card_id=10639, title='Ikoma Jeiku', force=3, chi=3, personal_honor=2, gold_cost=5, honor_requirement=0, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br>Ririko enters play ignoring Honor Requirement if you are a Unicorn Clan player.'
Kitsu_Ririko = Personality(card_id=10640, title='Kitsu Ririko', force=1, chi=4, personal_honor=3, gold_cost=5, honor_requirement=7, clan=[LionClan], keywords=[Destined, Shugenja, Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])