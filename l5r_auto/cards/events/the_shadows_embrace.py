from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Political, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, search your Fate deck or discard pile for a card titled Blood of the Preserver, show it, and put it into your hand.'
Discovering_the_Temple = Event(card_id=9791, title='Discovering the Temple', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your third turn from now ends, you have the trait, "In your Dynasty Phase, one time for each of your Provinces destroyed this game, you may refill one of your Provinces face-up."'
Distant_Expansion = Event(card_id=9792, title='Distant Expansion', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until the game ends, at the end of phase, lower each player's Honor to what it was at the start of that phase plus 3 plus any Honor he gained from battle resolution that phase; this Honor loss will not be negated, substituted, or reduced."
On = Event(card_id=9793, title='On', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose two Personalities controlled by the same player. Until the game ends, they may not be assigned, and will not move, to each other's battlefields."
StarCrossed_Lovers = Event(card_id=9794, title='Star-Crossed Lovers', keywords=[Unique, Political], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Until the game ends, before the second or later time each turn another player's card's effect bows any of your Personalities during the Action Phase, negate that effect, and before the second or later time each turn another player's card's effect prevents any of your Personalities from assigning, negate that effect."
Wartime_Preparations = Event(card_id=9795, title='Wartime Preparations', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])