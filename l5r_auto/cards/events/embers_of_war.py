from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Political, Unique, Winter
from l5r_auto.legality import EmperorEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, you may search your Fate deck for a non-Unique Strategy with a Political ability, show it, put it in your hand, and discard a card.'
Gaining_Advantage = Event(card_id=2759, title='Gaining Advantage', keywords=[Unique, Political, Winter], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, destroy all non-Unique Holdings with a printed Gold Cost of 0 and, until the game ends, Holdings in and out of play have a minimum Gold Cost of 1.'
Growing_Hostility = Event(card_id=2911, title='Growing Hostility', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, search your Dynasty deck for a Sensei Personality. Refill this Province with him, face-up.'
In_Search_of_Guidance = Event(card_id=3723, title='In Search of Guidance', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until the game ends, other players' actions will not discard cards from your hand, and if a player has resolved two actions that put cards in his hand in one phase, no more cards will be put into his hand that phase."
The_Scorpion_Wall_is_Finished = Event(card_id=8298, title='The Scorpion Wall is Finished', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])