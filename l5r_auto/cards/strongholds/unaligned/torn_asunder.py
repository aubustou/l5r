from __future__ import annotations
from ..common import Stronghold
from l5r_auto.clans import Unaligned
from l5r_auto.keywords import Experienced, Imperial
from l5r_auto.legality import EmperorEdition, ModernEdition
'"Imperial" is a Clan Alignment, and it is your Clan Alignment. If no other player has an Imperial Stronghold, you begin the game with the Imperial Favor. After this card produces gold, you may not Recruit Personalities until the end of the Phase. You may not buy Personalities with Clan discount if Imperial is their only Clan Alignment <i>(this trait only has effect when using the Clan Discount optional rule)</i>. '
Journeys_End_Keep_Experienced = Stronghold(card_id=10406, title="Journey's End Keep", gold_production='5', starting_family_honor=8, province_strength=7, clan=[Unaligned], keywords=[Experienced('1'), Imperial], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])