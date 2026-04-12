from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Terrain
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Battle:</b> Target your unbowed Unique Samurai. Destroy one or more target enemy Followers with a total Force less than or equal to your Samurai's."
A_Champions_Strike = Strategy(card_id=8, title="A Champion's Strike", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])
'Before this battle resolves, bow all Followers at its battlefield with 2 or lower Force. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Ambush_Pits = Strategy(card_id=347, title='Ambush Pits', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, DiamondEdition, ModernEdition])
'<b>Interrupt:</b> After the action targets your bowed Personality, negate its remaining effects.'
Balance_in_Nothingness = Strategy(card_id=672, title='Balance in Nothingness', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, GoldEdition, OnyxEdition, DiamondEdition, ModernEdition])