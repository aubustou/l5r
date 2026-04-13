from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import Air, Artisan, Cavalry, Commander, Courtier, Duelist, Expendable, Experienced, Gardener, IronCrane, Magistrate, Orator, Reserve, Samurai, Scout, Shugenja, TurquoiseChampion, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<i>(Draw a card after your Expendable card is destroyed.)</i><br>Your Political actions may not target Umehiko.'
Asahina_Umehiko = Personality(card_id=10837, title='Asahina Umehiko', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[CraneClan], keywords=[Expendable, Air, Gardener, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Home Battle:</b> If Gensai would be opposed, move him to the current battlefield. After he moves, you may discard a card to make a Ranged Attack with strength equal to the card's Focus Value."
Daidoji_Gensai = Personality(card_id=10838, title='Daidoji Gensai', force=2, chi=3, personal_honor=2, gold_cost=6, honor_requirement=2, clan=[CraneClan], keywords=[Cavalry, IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"Mantis Clan players ignore Tametaka's Honor Requirement.<br><b>Battle:</b> Give a target enemy Personality three -1F tokens."
Daidoji_Tametaka_Experienced_2 = Personality(card_id=10839, title='Daidoji Tametaka', force=5, chi=3, personal_honor=2, gold_cost=10, honor_requirement=2, clan=[CraneClan], keywords=[Experienced('2'), Unique, Commander, IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited, :bow::</b> Straighten a target Honor-producing Holding that has not produced Gold this turn.'
Doji_Kurohime = Personality(card_id=10840, title='Doji Kurohime', force=0, chi=3, personal_honor=2, gold_cost=4, honor_requirement=6, clan=[CraneClan], keywords=[Courtier], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"After another player's turn begins, straighten Tatsuki."
Doji_Tatsuki_Experienced = Personality(card_id=10841, title='Doji Tatsuki', force=2, chi=5, personal_honor=4, gold_cost=8, honor_requirement=10, clan=[CraneClan], keywords=[Unique, Artisan, Courtier, Experienced('1'), Orator, Samurai, TurquoiseChampion], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i><br>Ujirou enters play for 2 less Gold if any other player is Mantis Clan. Ujirou enters play for 4 less Gold if you are the Defender.'
Kakita_Ujirou = Personality(card_id=10842, title='Kakita Ujirou', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=2, clan=[CraneClan], keywords=[Duelist, Reserve, Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])