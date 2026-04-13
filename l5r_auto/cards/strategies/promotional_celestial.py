from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Kolat
from l5r_auto.legality import CelestialEdition, EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Absent Battle:</b> Target your performing Personality at any location and discard a card to move him to the current battlefield. Straighten his unit after this moves him.'
A_Brave_New_World = Strategy(card_id=4, title='A Brave New World', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target an enemy Personality or Follower: Give it -3F. Bow it if its Force is now 0.'
Costly_Feud = Strategy(card_id=1521, title='Costly Feud', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'This card has -1 Gold Cost if you control a Merchant.<br><b>Limited:</b> Target a Holding with a base Gold Cost of 4 or less controlled by a player who controls five or more Holdings: Destroy it.'
Economic_Manipulation = Strategy(card_id=2279, title='Economic Manipulation', gold_cost=4, focus_value=2, keywords=[Kolat], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Target an unaligned Personality: Give him -3F.<br><b>Battle:</b> Choose your performing Human Personality and target a Nonhuman Personality: Move it home.'
Folklore = Strategy(card_id=2621, title='Folklore', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Open:</b> Choose your performing Samurai: Permanently give him either <b>Cavalry</b> or <b>Tactician</b>.'
Gaining_Experience = Strategy(card_id=2760, title='Gaining Experience', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> Target two Personalities: You may transfer one or more tokens from one to the other. Destroy each of the two that now has a Fire, Poison, and Sake token.'
Green_Nightshade_Blend = Strategy(card_id=2904, title='Green Nightshade Blend', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After the resolution of your Battle, Limited, or Open action that created a non-Shadowlands Personality: Create a 2F/2C/2PH <b>Samurai</b> Personality with your Clan alignment at the same location.'
Lying_in_Ambush = Strategy(card_id=4788, title='Lying in Ambush', gold_cost=0, focus_value=3, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After another player's Battle action targets one of your attachments: Negate the attachment's destruction from the action's effects.<br><b>Reaction:</b> When paying for an attachment: Produce 2 Gold."
Near_Miss = Strategy(card_id=5523, title='Near Miss', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Choose your performing Personality and target a bowed card in his unit <i>(which may be him)</i>: Before this battle's resolution, straighten the targeted card."
Quick_Recovery = Strategy(card_id=6132, title='Quick Recovery', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Limited:</b> A target player discards a card at random.'
Unwelcome_Supervision = Strategy(card_id=9032, title='Unwelcome Supervision', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])