from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Brute, Earth, Experienced, Extortionist, Loyal, Magistrate, Naval, Samurai, Scout, Sensei, Shugenja, Thunder, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Reaction:</b> After Haruki enters play: Create a 2F/2C/3PH <b>Mantis Clan &#149; Nonhuman &#149; Deer &#149; Spirit</b> Personality with the ability, "<b>Limited:</b> If another player has higher Family Honor than you: Gain 2 Honor."'
Kitsune_Haruki = Personality(card_id=4462, title='Kitsune Haruki', force=0, chi=2, personal_honor=3, gold_cost=6, honor_requirement=4, clan=[MantisClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow Tomiko or one of her Spells: Ranged 6 Attack.'
Moshi_Tomiko = Personality(card_id=5286, title='Moshi Tomiko', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=0, clan=[MantisClan], keywords=[Naval, Shugenja, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Shichiro enters play: Discard all your other Sensei Personalities.<br>After a Ranged Attack action resolves that your Mantis Clan Personality performed: Once per battle, you may move him home.'
Tsuruchi_Shichiro = Personality(card_id=8878, title='Tsuruchi Shichiro', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Loyal, Naval, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Tsuruchi_Shigekazu = Personality(card_id=8879, title='Tsuruchi Shigekazu', force=6, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Twice per turn: Ranged 4 Attack.'
Tsuruchi_Tomaru_Experienced = Personality(card_id=8894, title='Tsuruchi Tomaru', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Unique, Experienced('1'), Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target an enemy card without attachments, and you may pay Gold equal to its Gold Cost: Bow it. If you paid the Gold, destroy it.'
Yoritomo_Kanaye = Personality(card_id=9579, title='Yoritomo Kanaye', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Brute, Extortionist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])