from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Earth, Iaijutsu, Kharmic, Kiho, Political, Terrain, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Iaijutsu Limited, :g2::</b> Your target unbowed Personality challenges a target Personality. The challenge may be refused unless exactly one of the targets is Fallen or The Dark Naga. Destroy the duel's loser."
A_Magistrate_Falls = Strategy(card_id=10559, title='A Magistrate Falls', gold_cost=2, focus_value=2, keywords=[Iaijutsu], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :g2::</b> Target your unbowed Tactician. Search your Fate deck for a non-Unique Battle Strategy and take an additional action to play it.'
Death_of_the_Winds = Strategy(card_id=10544, title='Death of the Winds', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle, :gstar::</b> Ranged Attack with strength equal to the amount you paid minus two.'
Deliberations = Strategy(card_id=10548, title='Deliberations', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Political Limited:</b> Bow your target unbowed Courtier. Discard the top card of another player's Fate deck. A target player gains or loses Honor equal to the discarded card's Focus Value or 3, whichever is lower. If he lost Honor, he ignores Honor Requirements this game."
Delicate_Gamble = Strategy(card_id=10545, title='Delicate Gamble', focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Discard the top card of a Fate deck. Target a card without attachments in a unit. If the discarded card's Focus Value is odd, bow the target <i>(0 is even)</i>. Otherwise, straighten it. Move its unit home if the target has a Madness token."
Fires_of_Turmoil = Strategy(card_id=10552, title='Fires of Turmoil', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(<b>Limited, :g2::</b> Discard a Kharmic card from your hand to draw a card.)</i><br><b>Limited:</b> Until your next turn begins, before each time a player gains Honor, reduce the gain by 1 unless he controls a Spirit.'
Invocation = Strategy(card_id=10547, title='Invocation', focus_value=3, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Bow your target unbowed Personality. Destroy a target enemy unit with lower total Force than your Personality's <i>(current)</i> Force.<br>."
Looming_Danger = Strategy(card_id=10551, title='Looming Danger', focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle, :g1::</b> Target your Personality at home. If he would be opposed, move him to the current battlefield. If he is a Yojimbo, give him <b>Expendable </b><i>(this turn)</i>.'
Moments_of_Destiny = Strategy(card_id=10560, title='Moments of Destiny', gold_cost=1, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"After this battle resolves, if its Province was not destroyed, destroy the targets of this card's action. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play. Target zero to two attacking cards.<br>"
No_Way_Out = Strategy(card_id=10546, title='No Way Out', focus_value=3, keywords=[Terrain], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Each player shuffles his hand into his deck, then draws as many cards as he shuffled into his deck.'
Overwhelming_Chaos = Strategy(card_id=10549, title='Overwhelming Chaos', focus_value=4, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Earth Battle:</b> Target your unbowed Monk. Melee Attack with strength equal to his Force, which may target a card in the Defender's home.<br>."
Strength_in_the_Earth = Strategy(card_id=10556, title='Strength in the Earth', focus_value=2, keywords=[Earth, Kiho], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target your opposed unbowed Paragon. Give him +2F or +2PH. Melee Attack with strength equal to his Force or Personal Honor.<br>.'
Strength_of_the_Divine = Strategy(card_id=10555, title='Strength of the Divine', focus_value=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(<b>Limited, :g2::</b> Discard a Kharmic card from your hand to draw a card.)</i><br><b>Limited:</b> Permanently give your target non-Loyal, face-up Personality in or out of play your Clan Alignment.'
Suikihimes_Sanction = Strategy(card_id=10557, title="Suikihime's Sanction", focus_value=4, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'If you do not control a Cavalry unit here, negate each Battle action taken by a player without units here.<br><b>Battle/Engage:</b> Destroy a Terrain <i><i><i>(if able)</i></i></i>. Put this Terrain into play.'
Temple_Grounds = Strategy(card_id=10554, title='Temple Grounds', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(<b>Limited, :g2::</b> Discard a Kharmic card from your hand to draw a card.)</i><br><b>Open:</b> Until the game ends, a player must pay 2 Gold to draw a card from effects of his own Strategies during an Action Phase.<br><b>Open:</b> No player can gain Honor in Action Phases <i>(this turn)</i>.<br>'
The_Heavens_Blessing = Strategy(card_id=10558, title="The Heavens' Blessing", focus_value=4, keywords=[Kharmic], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow your target unbowed Personality. Bow a target enemy card. If your Personality is Fallen or a Magistrate, straighten him before this battle resolves.'
The_Tale_of_the_Disgraced = Strategy(card_id=10553, title='The Tale of the Disgraced', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Limited, :g4::</b> Discard the top card of a Fate deck. You may target a Personality and give him a Chi penalty equal to the card's Focus Value. If this destroyed the target, his controller puts this Strategy in his hand."
Unbearable_Weight = Strategy(card_id=10550, title='Unbearable Weight', gold_cost=4, focus_value=1, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])