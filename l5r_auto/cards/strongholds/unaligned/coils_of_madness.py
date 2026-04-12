from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import Unaligned
from l5r_auto.legality import EmperorEdition, ModernEdition
'If there is no other Foothold of the Mad player, you go first. You do not lose Honor from cards you own. Fallen Personalities join you for 2 less Gold. Personalities and Followers have -1F for each of their Madness tokens.<br><b>Limited, :bow:</b>: Give a target card a <b>Madness </b>token.<br><b>Limited, :bow:</b>: Your Holdings enter play paying 2 less Gold <i>(this turn)</i>.'
Foothold_of_the_Mad = Stronghold(card_id=10562, title='Foothold of the Mad', gold_production='0', starting_family_honor=0, province_strength=0, clan=[Unaligned], traits=[], abilities=[], legality=[EmperorEdition])
'Your non-Unique Monk and Fudo Personalities in and out of play have <b><b>Monk &#149; Fudo</b></b>. Fudo Personalities join you for 2 less Gold. You ignore Honor Requirements of your Fudo cards. You do not lose Honor from Fudo cards you own. You may not win by Enlightenment. <br><b>Limited, :bow::</b> Search your discard pile or deck for a Fudo Ring, show it, and put it in your hand.'
The_False_Path = Stronghold(card_id=10561, title='The False Path', gold_production='3', starting_family_honor=0, province_strength=9, clan=[Unaligned], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])