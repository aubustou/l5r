from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Air, ClanChampion, Commander, Courtier, Elite, Inexperienced, Loyal, Ninja, Samurai, ShojusSoul, Shugenja, Sociopath, SoulOf, Unique, Villain
from l5r_auto.legality import EmperorEdition, ModernEdition
'<i>(Elite cards contribute Force even if bowed.)</i>'
Bayushi_Kasumi = Personality(card_id=10247, title='Bayushi Kasumi', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[ScorpionClan], keywords=[Elite, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle/Limited:</b> Look at the top card of your Fate deck. If it is an attachment, you may attach it to one of your Personalities at Nitoshi's location, paying all costs. If it is a Strategy, you may take an additional action to play it <i>(if legal)</i>."
Bayushi_Nitoshi_Inexperienced = Personality(card_id=10248, title='Bayushi Nitoshi', force=6, chi=4, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Unique, ClanChampion, Courtier, Inexperienced, Samurai, ShojusSoul, Sociopath], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Even if Utoro is bowed, discard a card and target a Personality: Straighten him.'
Bayushi_Utoro = Personality(card_id=10249, title='Bayushi Utoro', force=4, chi=4, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Samurai, SoulOf('Bayushi Motomu')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Even if Chikata is bowed, target a Scorpion Clan or Dragon Clan Personality: Bow or straighten him.'
Shosuro_Chikata = Personality(card_id=10250, title='Shosuro Chikata', force=3, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja, SoulOf('Bayushi Kasata')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target a Follower in your discard pile: Attach it to Haruto, paying 2 less Gold.'
Yogo_Haruto = Personality(card_id=10251, title='Yogo Haruto', force=5, chi=4, personal_honor=0, gold_cost=9, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Unique, Air, Commander, Shugenja, Villain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])