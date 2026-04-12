from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Alchemist, Courtier, Duelist, Earth, Elite, Experienced, FavoredOfTheFireDragon, Imperial, ImperialExplorer, Kensai, Magistrate, Monk, Samurai, Scout, Sensei, Shugenja, Tattooed, Unique, Water
from l5r_auto.legality import EmperorEdition, ModernEdition
'Kojinrue may be assigned even if bowed.<br>You may choose Kojinrue to perform actions requiring an unbowed performer even if he is bowed.'
Mirumoto_Kojinrue_Experienced = Personality(card_id=10284, title='Mirumoto Kojinrue', force=5, chi=4, personal_honor=2, gold_cost=10, honor_requirement=4, clan=[DragonClan], keywords=[Elite, Kensai, Unique, Experienced('1'), Imperial, ImperialExplorer, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Open:</b> Target another player's Doji Iza: Kyoshiro duels her. Destroy the duel's loser."
Mirumoto_Kyoshiro = Personality(card_id=10285, title='Mirumoto Kyoshiro', force=3, chi=3, personal_honor=3, gold_cost=6, honor_requirement=5, clan=[DragonClan], keywords=[Duelist, Courtier, Magistrate], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(Elite cards contribute Force even if bowed.)</i>'
Mirumoto_Yonekura = Personality(card_id=10286, title='Mirumoto Yonekura', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=5, clan=[DragonClan], keywords=[Elite, Kensai, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Yozo enters play or overlays: Discard all your other Sensei Personalities.<br>After your Iaijutsu action resolves: Give any Personality who performed it +2F.'
Mirumoto_Yozo_Experienced_2 = Personality(card_id=10287, title='Mirumoto Yozo', force=5, chi=5, personal_honor=2, gold_cost=10, honor_requirement=4, clan=[DragonClan], keywords=[Duelist, Experienced('2'), Unique, FavoredOfTheFireDragon, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> If Tsuchiya is defending, destroy one of his Spells: Give him <b>Stalwart </b>and a Force bonus equal to his current Force. <i>(Stalwart cards negate their first bowing each turn by other players' cards)</i>."
Tamori_Tsuchiya = Personality(card_id=10288, title='Tamori Tsuchiya', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[DragonClan], keywords=[Alchemist, Earth, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality: Move him home.'
Togashi_Mihato = Personality(card_id=10289, title='Togashi Mihato', force=4, chi=4, personal_honor=1, gold_cost=8, honor_requirement=0, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Monk, Tattooed, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])