from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Terrain
from l5r_auto.legality import DiamondEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'While there is exactly one defending Personality here, he has the ability, "<b>Repeatable Battle:</b> Challenge a target enemy Personality. Destroy the loser" and each player has the ability, "<b>Repeatable Battle:</b> Move home your target attacking Personality. Bow him as he moves."<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play. Take an additional action granted by it.'
Come_One_at_a_Time = Strategy(card_id=1434, title='Come One at a Time', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, GoldEdition, JadeEdition, DiamondEdition, ModernEdition])
'<b>Political Interrupt:</b> Negate the action if it is Political and taken by a player whose total Force of all units at home is now less than your total Force of all units at home <i>(bowed cards count)</i>.'
Outmaneuvered_by_Force = Strategy(card_id=5832, title='Outmaneuvered by Force', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, GoldEdition, OnyxEdition, DiamondEdition, ModernEdition])
'<b>Political Open:</b> Bow your target unbowed Magistrate Personality. Bow a target Human Personality with lower Personal Honor.'
Rank_Hath_Privilege = Strategy(card_id=6162, title='Rank Hath Privilege', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, JadeEdition, OnyxEdition, ModernEdition])
'<b>Iaijutsu Battle:</b> Your target unbowed Human Personality challenges a target enemy Human Personality to a duel of Personal Honor. The winner gains 2 Honor. Dishonor the loser. Move him home. Bow him as he moves.'
Show_Me_Your_Stance = Strategy(card_id=7194, title='Show Me Your Stance', focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, JadeEdition, OnyxEdition, DiamondEdition, ModernEdition])
'Before your turn ends, if this Strategy is in your discard pile, put it in your hand.'
The_Path_of_Wisdom = Strategy(card_id=8251, title='The Path of Wisdom', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, ImperialEdition, OnyxEdition, DiamondEdition, ModernEdition])
"<b>Battle:</b> If a target Samurai's army contains any Shadowlands cards, bow and dishonor him, and permanently give him <b>Shadowlands</b>."
You_Walk_with_Evil = Strategy(card_id=9686, title='You Walk with Evil', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, ImperialEdition, OnyxEdition, ModernEdition])