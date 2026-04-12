from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Cavalry, Courtier, Experienced, Loyal, Magistrate, Ninja, Paragon, Samurai, Seductress, Sensei, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, ModernEdition
'Crab Clan players may control Hamada.<br>Hamada has +1F for each of your Personalities who is Crab Clan or a Courtier.'
Bayushi_Hamada = Personality(card_id=10308, title='Bayushi Hamada', force=5, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After Kazutoshi enters play or overlays: Discard all your other Sensei Personalities.<br>Before the first time each turn another player's card's effect destroys one of your Loyal Personalities: Negate the destruction. Move him home. Bow him. Dishonor him."
Bayushi_Kazutoshi_Experienced_2 = Personality(card_id=10309, title='Bayushi Kazutoshi', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=1, clan=[ScorpionClan], keywords=[Experienced('2'), Loyal, Unique, Courtier, Samurai, Sensei], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> When another player would target a Magistrate at Wakui's battlefield with an action: The action targets Wakui instead, if legal."
Bayushi_Wakui = Personality(card_id=10310, title='Bayushi Wakui', force=1, chi=3, personal_honor=1, gold_cost=4, honor_requirement=0, clan=[ScorpionClan], keywords=[Magistrate, Samurai, Yojimbo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Political Open:</b> Bow Makiko: Take the Imperial Favor.<br><b>Political Reaction:</b> Before an action resolves, bow Makiko: Reduce all Honor gains from it by 2.'
Shosuro_Makiko_Experienced = Personality(card_id=10311, title='Shosuro Makiko', force=2, chi=4, personal_honor=1, gold_cost=9, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Unique, Courtier, Experienced('1'), Seductress], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'While Tanihara is attacking at a battlefield, its province has a maximum strength equal to its base strength.'
Shosuro_Tanihara = Personality(card_id=10312, title='Shosuro Tanihara', force=3, chi=2, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Personality: Give him <b>Brash </b><i>(the Defender may draw a card after a Brash card is assigned to attack)</i>.'
Soshi_Shinoko = Personality(card_id=10313, title='Soshi Shinoko', force=2, chi=4, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[ScorpionClan], keywords=[Cavalry, Courtier], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])