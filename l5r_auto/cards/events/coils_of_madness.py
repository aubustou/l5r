from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until the game ends, each player has the ability, "<b>Open:</b> Your target Personality with a Madness token commits Seppuku" and any player who ends his turn with 20 or more Madness tokens on his Personalities loses the game.'
An_Empire_of_Madness = Event(card_id=10426, title='An Empire of Madness', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Until the game ends, each player draws two cards instead of one at the end of his turn if he put no other cards in his hand that turn.'
An_End_to_Hostilities = Event(card_id=10424, title='An End to Hostilities', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Search your Fate deck for two attachments with different titles. Show them. Another player chooses one of them and removes it from the game. Put the other attachment in your hand.'
Dark_Audience = Event(card_id=10420, title='Dark Audience', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Limited:</b> Until your next turn begins, other players' cards will not destroy your Personalities in a defending army."
Rampant_Paranoia = Event(card_id=10421, title='Rampant Paranoia', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Each player targets and bows an unbowed Samurai.'
Riot_in_the_Second_City = Event(card_id=10422, title='Riot in the Second City', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Limited:</b> Target two Unique Personalities in play, exactly one of which is yours. Your Personality challenges the other Personality. Destroy the duel's loser."
The_Empires_Foe_Exposed = Event(card_id=10423, title="The Empire's Foe Exposed", keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Until your second turn from now begins, once per turn, you may take a Limited action on a Strategy as an <b>Open</b> action.'
The_Madness_Spreads = Event(card_id=10419, title='The Madness Spreads', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Until the game ends, this Province does not hold Dynasty cards and has +10 Province Strength.'
The_Second_Battle_of_Beiden_Pass = Event(card_id=10425, title='The Second Battle of Beiden Pass', keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])