from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Dojo, Experienced, Forest, Fudo, Imperial, Kharmic, Retainer, Temple, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'This Holding enters play bowed. <i>(It straightens normally on your first turn.)</i><br>:bow:: Produce 0 Gold. Give this Holding a +1 Gold Production <b>Wealth </b>token.'
Bamboo_Harvesters_Experienced_2 = Holding(card_id=10428, title='Bamboo Harvesters', gold_cost=0, keywords=[Experienced('2'), Unique, Forest], traits=[], abilities=[], legality=[EmperorEdition])
':bow:: Produce 2 Gold, or 3 Gold if paying for a Holding which may only pay for that card.<br><b>Limited:</b> Once or twice during your first turn <i>(only)</i>, put one or more cards in your Provinces at the bottom of your deck, refilling them face-up.'
Border_Keep_Experienced_2 = Holding(card_id=10429, title='Border Keep', gold_cost=0, keywords=[Experienced('2'), Unique], traits=[], abilities=[], legality=[EmperorEdition])
'<b>:bow::</b> When paying for a non-Unique Samurai, he enters play for 0 Gold.'
Colonial_Dojo = Holding(card_id=10432, title='Colonial Dojo', gold_cost=7, keywords=[Dojo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Holding has +2GP when it pays for a single attachment only.'
Colonial_Temple = Holding(card_id=10433, title='Colonial Temple', gold_cost=3, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<i>(<b>Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i><br><b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Destroy a Madness token.'
Fudoist_Advisor = Holding(card_id=10427, title='Fudoist Advisor', gold_cost=2, keywords=[Kharmic, Fudo, Retainer], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Battle:</b> Move a target attacking Personality home. Destroy this Holding.'
Questionable_Merchant = Holding(card_id=10434, title='Questionable Merchant', gold_cost=3, keywords=[Retainer], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Battle/Open, :gstar:, :bow::</b> Equip a Follower, paying 2 less Gold.'
Recruitment_Station = Holding(card_id=10430, title='Recruitment Station', gold_cost=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold, or 4 Gold if paying for a Unique Personality which may only pay for him.<br><b>Limited, :bow::</b> Gain 1 Honor.<br>'
Suikihimes_Chambers = Holding(card_id=10436, title="Suikihime's Chambers", gold_cost=3, keywords=[Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Give a target card a <b>Madness </b>token.'
Temple_of_Madness = Holding(card_id=10435, title='Temple of Madness', gold_cost=2, keywords=[Temple], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold.<br><b>Limited, :bow::</b> Draw a card. Discard a card.'
Temple_of_Tengen = Holding(card_id=10431, title='Temple of Tengen', gold_cost=2, keywords=[Unique, Temple], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])