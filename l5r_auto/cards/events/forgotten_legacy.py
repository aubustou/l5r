from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your turn two turns from now begins, all players have the ability, "<b>Battle:</b> Target your performing unbowed attacking Personality and bow all unbowed cards in his unit to destroy a target enemy card without attachments."'
Assault_in_the_Jungle = Event(card_id=628, title='Assault in the Jungle', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, any player who controls the Imperial Favor discards it, until your turn two turns from now begins, actions that discard the Imperial Favor as a condition upon further effects have their effects negated if they target a Nonhuman Personality, and until the game ends, Nonhumans may not perform Political actions.'
Burning_Dreams = Event(card_id=1185, title='Burning Dreams', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After your next turn begins, permanently give each of your provinces +2 strength.'
Willing_Spirits = Event(card_id=9337, title='Willing Spirits', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])