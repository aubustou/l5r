from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Air, AmethystChampion, Courtier, Duelist, Earth, Experienced, Fire, Henshin, Inquisitor, Magistrate, Monk, Samurai, Shugenja, Unique, Villain, Water, Yojimbo
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Political Limited:</b> Take the Imperial Favor.<br><b>Battle/Limited:</b> Target another player's card in a unit: Bow the target. If it is Kolat, Ninja, or Shadowlands, choose a player who gains or loses 2 Honor."
Asako_Izuna_Experienced = Personality(card_id=10302, title='Asako Izuna', force=3, chi=4, personal_honor=3, gold_cost=9, honor_requirement=6, clan=[PhoenixClan], keywords=[Unique, Air, AmethystChampion, Courtier, Experienced('1'), Inquisitor, Magistrate, Shugenja, Villain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Kyuudo has +3F and <b>Elite</b> while defending <i>(Elite cards contribute Force even if bowed)</i>.'
Asako_Kyuudo = Personality(card_id=10303, title='Asako Kyuudo', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[PhoenixClan], keywords=[Earth, Inquisitor, Magistrate, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target a Holding: It produces 1 additional Gold when it bows to produce Gold <i>(this turn)</i>.'
Asako_Suzukaze = Personality(card_id=10304, title='Asako Suzukaze', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Air, Henshin, Monk], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(Shugenja may attach and cast Spells.)</i><br><b>Fire Battle/Open:</b> Give Hibana -3F. Give your target non-Water Personality +3F.'
Isawa_Hibana = Personality(card_id=10305, title='Isawa Hibana', force=3, chi=3, personal_honor=2, gold_cost=6, honor_requirement=6, clan=[PhoenixClan], keywords=[Fire, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
Isawa_Mizuhama = Personality(card_id=10306, title='Isawa Mizuhama', force=2, chi=2, personal_honor=2, gold_cost=4, honor_requirement=6, clan=[PhoenixClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Bow your performing Shugenja: Give Tetsaka <b>Cavalry</b> or <b>Naval</b>.'
Shiba_Tetsaka = Personality(card_id=10307, title='Shiba Tetsaka', force=4, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[PhoenixClan], keywords=[Duelist, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])