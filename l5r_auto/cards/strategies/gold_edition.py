from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Terrain
from l5r_auto.legality import GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Interrupt:</b> Negate the action's Fear effects."
A_Stout_Heart = Strategy(card_id=84, title='A Stout Heart', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'The Attacker and Defender each have the ability, "<b>Absent Repeatable Battle:</b> Move your target Personality at any location to this battlefield." <br><b>Absent Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Accessible_Terrain = Strategy(card_id=108, title='Accessible Terrain', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
"As a Focus Effect, discard all focused cards <i>(their unresolved Focus Effects don't happen)</i>, and end this duel now, without resolution."
Another_Time = Strategy(card_id=410, title='Another Time', focus_value=0, traits=[], abilities=[], legality=[ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, TwentyFestivalsEdition])
'Your Personalities at this battlefield have +1F. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Contentious_Terrain = Strategy(card_id=1475, title='Contentious Terrain', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
"<b>Political Interrupt:</b> Target your unbowed Samurai. Before the other player's action causes you an Honor loss, negate it, and your Samurai may then issue a challenge. The player may either target his unbowed Personality to accept the challenge or refuse. If the player refuses or loses the duel, he loses Honor equal to the amount you negated. Destroy the loser."
Defend_Your_Honor = Strategy(card_id=1923, title='Defend Your Honor', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
"Your Ranged Attacks have +1 strength. Other player's Ranged Attacks have -1 strength. <br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play."
Higher_Ground = Strategy(card_id=3273, title='Higher Ground', gold_cost=0, focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>Interrupt, :g2::</b> If the action is on an Assassin, Kolat, or Ninja card, then after it targets you, your cards or your tokens, negate its remaining effects except for Honor losses to its player, and he loses 5 Honor.'
Investigation = Strategy(card_id=3797, title='Investigation', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>Limited:</b> Permanently remove all Clan Alignments from all your Human Personalities without your Clan Alignment, permanently give them your Clan Alignment, and give them each a +1F/+1C token.'
Oath_of_Fealty = Strategy(card_id=5641, title='Oath of Fealty', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>Interrupt:</b> After an action on a Kiho, Shugenja, or Spell targets your cards, negate its remaining effects.'
Resist_Magic = Strategy(card_id=6271, title='Resist Magic', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'<b>Open:</b> Bow a target Shadowlands Personality.'
Shadowlands_Sickness = Strategy(card_id=6674, title='Shadowlands Sickness', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition, OnyxEdition])
'<b>Battle:</b> Target your unbowed Personality with 3 or more Chi. Either move him to another unresolved battlefield or destroy a Terrain at the current battlefield.'
Superior_Tactics = Strategy(card_id=7660, title='Superior Tactics', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
'<b>Interrupt:</b> If the action is from or targets a Samurai and it has any effects, other than consequences of losing a duel, that may dishonor him or cause his player Honor losses, negate the action.'
The_Code_of_Bushido = Strategy(card_id=7989, title='The Code of Bushido', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
"<b>Interrupt:</b> Negate the action's Melee or Ranged Attacks."
The_Turtles_Shell = Strategy(card_id=8400, title="The Turtle's Shell", gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])