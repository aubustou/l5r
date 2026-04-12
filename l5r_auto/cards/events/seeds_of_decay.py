from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Festival, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose a Province. Permanently give it -2 strength and destroy any Region attached to it. Until the game ends, after a Region attaches to it, destroy the Region, and after a Holding enters play from it, give the Holding a -1GP token.'
Dark_Experiments = Event(card_id=10029, title='Dark Experiments', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your second turn from now begins, Personalities may not be targeted by the rulebook Cavalry player ability.'
Incredible_Tragedy = Event(card_id=10030, title='Incredible Tragedy', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, for each dead Personality in your discard pile, create a 2F/2C/3PH Samurai &#149; Ancestor &#149; Spirit Personality with your Clan Alignment. If this created no Personalities, you may shuffle this Event into your deck instead of discarding it normally.'
Offering_Reverence = Event(card_id=10031, title='Offering Reverence', keywords=[Unique, Festival], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your second turn from now begins, you have the ability, "<b>Limited:</b> Put a target Ring in your hand into play. While it remains in play, it does not count towards an Enlightenment Victory."'
Starting_on_the_Path = Event(card_id=10032, title='Starting on the Path', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])