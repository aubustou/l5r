from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Cavalry, Courtier, Destined, Expendable, Experienced, Fallen, Loyal, Magistrate, Ninja, Paragon, Samurai, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
Bayushi_Amorie = Personality(card_id=10653, title='Bayushi Amorie', force=4, chi=2, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Cavalry, Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"During battle resolution, Manami's army has +2F."
Bayushi_Manami_Experienced = Personality(card_id=10654, title='Bayushi Manami', force=2, chi=3, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Unique, Experienced('1'), Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g3:: Give Nigawa two +1F tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>'
Shosuro_Nigawa = Personality(card_id=10655, title='Shosuro Nigawa', force=2, chi=3, personal_honor=2, gold_cost=4, honor_requirement=0, clan=[ScorpionClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Bow your target unbowed Ninja Personality. Bow a target Personality; if he is Fudo or Fallen, he will not straighten this turn.'
Soshi_Kodanshi_Experienced = Personality(card_id=10656, title='Soshi Kodanshi', force=4, chi=4, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Unique, Experienced('1'), Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open:</b> If it is your turn or you control a Courtier, give a target Personality -2F.'
Yogo_Nobukai = Personality(card_id=10658, title='Yogo Nobukai', force=3, chi=3, personal_honor=1, gold_cost=5, honor_requirement=0, clan=[ScorpionClan], keywords=[Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br><i>(Draw a card after your Expendable card is destroyed.)</i><br>After Takashi enters play, lose 1 Honor.'
Yogo_Takashi = Personality(card_id=10657, title='Yogo Takashi', force=0, chi=4, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[ScorpionClan], keywords=[Destined, Expendable, Courtier, Fallen], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])