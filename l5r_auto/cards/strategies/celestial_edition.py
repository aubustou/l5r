from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Control, DarkVirtue, Forest, Insight, Kiho, Political, Terrain, Thunder, Winter
from l5r_auto.legality import CelestialEdition, DiamondEdition, GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, LotusEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'The snow blocks travel. Personalities cannot move to or from this battlefield. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Blanketed_Forest = Strategy(card_id=1020, title='Blanketed Forest', gold_cost=0, focus_value=1, keywords=[Forest, Terrain, Winter], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, CelestialEdition, SamuraiEdition, ModernEdition])
"<b>Dark Virtue Open, :g3::</b> Target your unbowed Samurai and target a Personality. While your Samurai remains unbowed and in play, negate the Personality's straightening."
Control = Strategy(card_id=1485, title='Control', focus_value=2, keywords=[Control], traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, CelestialEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'As a Focus Effect, bow the other Personality.<br><b>Battle:</b> Move your target opposed Personality home. Gain 1 Honor. Draw a card.'
Discretionary_Valor = Strategy(card_id=2014, title='Discretionary Valor', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
"<b>Bushido Virtue Interrupt:</b> If the action is another player's, destroy your target honorable Samurai to negate your target Personality's destruction from it."
Duty = Strategy(card_id=2250, title='Duty', focus_value=2, traits=[], abilities=[], legality=[LotusEdition, CelestialEdition, SamuraiEdition, DiamondEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition])
'<b>Interrupt:</b> Target your Yojimbo. The action targets him instead of another card, if legal.'
Final_Sacrifice = Strategy(card_id=2550, title='Final Sacrifice', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Dark Virtue Battle:</b> Target your Samurai. Look at the top three cards of any Fate deck. You may rearrange them. You may take an additional Battle action to play one of them that is a Battle Strategy.'
Insight = Strategy(card_id=3763, title='Insight', gold_cost=0, focus_value=3, keywords=[DarkVirtue, Insight], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Kiho Battle:</b> Target your unbowed Monk without a Weapon. Bow a target enemy Personality without a Weapon.'
Palm_Strike = Strategy(card_id=5867, title='Palm Strike', gold_cost=0, focus_value=3, keywords=[Kiho], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, CelestialEdition, GoldEdition, SamuraiEdition, DiamondEdition, ModernEdition])
'<b>Political Battle:</b> Move home a target Personality with 0 Personal Honor and, as he moves, his controller loses 2 Honor.'
Ramifications = Strategy(card_id=6157, title='Ramifications', gold_cost=0, focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Political Open:</b> After the next time a target Personality attacks you <i>(this turn)</i>, gain 2 Honor and dishonor him.'
Selfless_Politics = Strategy(card_id=6586, title='Selfless Politics', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, SamuraiEdition, ModernEdition])
"<b>Battle:</b> Target and bow your unbowed Kensai or one of his unbowed Weapons. Destroy a target enemy Follower, Item, or Personality without attachments, that has Force equal to or less than your Kensai's Chi."
Swift_Sword_Cut = Strategy(card_id=7694, title='Swift Sword Cut', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Kiho Thunder Battle:</b> Bow your target unbowed Monk or Shugenja. Ranged Attack with strength equal to his Chi.'
The_Wrath_of_OsanoWo = Strategy(card_id=8440, title='The Wrath of Osano-Wo', gold_cost=0, focus_value=3, keywords=[Kiho, Thunder], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, CelestialEdition, GoldEdition, JadeEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Bow your target unbowed Weapon. Destroy a target enemy attachment. <br><b>Battle:</b> Give a target Personality with a Weapon +2F.'
Tonfajutsu = Strategy(card_id=8632, title='Tonfajutsu', gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
"This ability's Gold cost is 0 if you control both a Cavalry unit and an Infantry unit at this battlefield.<br><b>Battle, :g3::</b> Straighten or bow a target Personality."
Versatile_Army = Strategy(card_id=9143, title='Versatile Army', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Target your Personality. You may not use abilities on cards in his unit or target them with actions. Before this battle resolves, double his Force and the Force of each Follower in his unit. Destroy him after the battle ends.'
Wedge = Strategy(card_id=9281, title='Wedge', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, LotusEdition, ImperialEdition, CelestialEdition, OnyxEdition, SamuraiEdition, DiamondEdition, ModernEdition])