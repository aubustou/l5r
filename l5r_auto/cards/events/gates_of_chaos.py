from __future__ import annotations
from .common import Event
from l5r_auto.keywords import Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'Personalities and Followers have -1F while attacking.<br><b>Limited:</b> Put this Event into play. Discard it after your next turn begins.'
A_Fever_in_the_Blood = Event(card_id=10603, title='A Fever in the Blood', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Defending players may not play Terrains <i>(this turn)</i>. After the first time you destroy a Province in battle this turn, if you do not have more Provinces than the Defender <i>(at that time)</i>, gain a Province.'
Journeys_End_Siege = Event(card_id=10604, title="Journey's End Siege", keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Your Cavalry Personalities and Followers have +1F while attacking and opposed <i>(this turn)</i>.'
Riding_to_the_Rescue = Event(card_id=10605, title='Riding to the Rescue', traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])