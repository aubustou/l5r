from __future__ import annotations
from .common import Holding
from l5r_auto.keywords import Boat, Dojo, Farm, Market, Port, Retainer, Singular
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
':bow:: Produce 2 Gold, or 4 Gold if paying for a Holding which may only pay for that card.'
Damaged_Port = Holding(card_id=10264, title='Damaged Port', gold_cost=2, keywords=[Port], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Open, :bow::</b> Give a target Personality <b>Cavalry</b>. Destroy this Holding if it is your turn.'
Green_Lake_Dojo = Holding(card_id=10265, title='Green Lake Dojo', gold_cost=2, keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction, :bow::</b> After another player's action resolves which destroyed one of your Personalities, gain 2 Honor."
Heros_Memorial = Holding(card_id=10266, title="Hero's Memorial", gold_cost=0, keywords=[Singular], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
':bow:: Produce 2 Gold.<br><b>Limited:</b> Target a card in a Province. If the card is not yours, bow this Holding to turn it face-up; otherwise, turn it face-up.'
Merchant_Outpost = Holding(card_id=10267, title='Merchant Outpost', gold_cost=2, keywords=[Market, Port], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target two of your Personalities. A lesson is taught. One copies Commander, Duelist, Kensai, Magistrate, Paragon, Scout, or Yojimbo from the other.'
Miryoku_no_Shima = Holding(card_id=10268, title='Miryoku no Shima', gold_cost=6, traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
':bow:: Produce 3 Gold.<br><b>Battle:</b> Raise to 4 the Force of a target Follower with a printed Gold Cost of 1 or more.'
The_Forgotten_Bay_Dojo = Holding(card_id=10269, title='The Forgotten Bay Dojo', gold_cost=4, keywords=[Dojo], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After an action resolves whose effects destroyed your Follower with a Gold Cost of 1 or more, you may put it face-up under this card.<br><b>Repeatable Battle/Limited, :gstar::</b> Equip a Follower from under this card to your target Personality.'
The_Tachikaze = Holding(card_id=10270, title='The Tachikaze', gold_cost=0, keywords=[Boat, Retainer], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 2 Gold. If you bowed this Holding while paying to Recruit a Farm Holding, refill the Province face-up.'
Vast_Paddy_Fields = Holding(card_id=10271, title='Vast Paddy Fields', gold_cost=2, keywords=[Farm], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])