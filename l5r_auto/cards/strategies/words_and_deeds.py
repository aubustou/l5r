from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
"<b>Political Open:</b> Destroy your target unbowed Courtier Personality with 3 or more Personal Honor. After each time <i>(this turn)</i> another player's target Personality assigns or an action on a card in his unit resolves, dishonor him and gain 3 Honor."
An_Act_of_Disdain = Strategy(card_id=351, title='An Act of Disdain', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Choose your performing Personality and target a Follower in your hand or discard pile: Attach it to him, paying 1 less Gold.'
Inspirational_Address = Strategy(card_id=3767, title='Inspirational Address', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, SamuraiEdition, ModernEdition])
"<b>Battle:</b> Target your unbowed Samurai Personality. Bow a target enemy unit with lower total Force than your Samurai's Force.While your Samurai remains unbowed and at the current battlefield, negate the straightening of any cards in the enemy unit."
Rewards_of_Experience = Strategy(card_id=6308, title='Rewards of Experience', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'<b>Kiho Water Battle:</b> Move your target unbowed Monk or Shugenja to another location.'
The_Emperors_Road = Strategy(card_id=8057, title="The Emperor's Road", focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Target your unbowed defending Personality. Move home a target enemy Personality with lower Personal Honor. Gain 2 Honor.'
Usurpation = Strategy(card_id=9050, title='Usurpation', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])