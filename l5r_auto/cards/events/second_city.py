from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, after the next time this game your Honor is below its starting value, <i>you have a tea ceremony</i>; gain 5 Honor.'
Formal_Apology = Event(card_id=2660, title='Formal Apology', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, you may destroy this Province to draw three cards.'
Harsh_Choices = Event(card_id=2978, title='Harsh Choices', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your second turn from now begins, the Attacker may not announce a Battle action before the Defender's first normal opportunity to act or pass in a battle."
Rebuilding_Kyuden_Hida = Event(card_id=6200, title='Rebuilding Kyuden Hida', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Until your second turn from now begins, all provinces have a maximum strength equal to their base strength, and after each time another player who controls no units at the current battlefield announces a Battle action, he discards a card.'
Times_of_Strife = Event(card_id=8494, title='Times of Strife', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Until your second turn from now begins, after the resolution of the first action each phase that one or more Personalities performed, bow them.'
War_Weariness = Event(card_id=9222, title='War Weariness', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])