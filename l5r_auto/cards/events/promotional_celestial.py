from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
"After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, choose another player's Personality in play. After the next time this game his unit is assigned or an action resolves that he performed, dishonor him, and his controller loses 2 Honor."
Minor_Blackmail = Event(card_id=5061, title='Minor Blackmail', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, until your turn two turns from now begins, after each time an Unaligned Human Personality turns face-up in one of your Provinces, permanently give him your Clan Alignment. <i>He has sworn fealty to you.</i>'
Open_Recruitment = Event(card_id=5762, title='Open Recruitment', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After you reveal cards in your Provinces at the start of your turn, if this Event is face-up in one of them, look at the top four cards of any Fate deck. You may discard one of them. Put the rest back in any order.'
Signs_and_Portents = Event(card_id=7253, title='Signs and Portents', keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])