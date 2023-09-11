from __future__ import annotations

from l5r_auto.keywords import Kharmic
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Event

"Reduce all Honor gains and losses from Holdings by 1 <i>(minimum zero)</i>.<br><b>Open:</b> Put this Event into play. Discard it before your next turn ends. You may target and dishonor a Crane Clan Personality."
Abdication = Event(
    card_id=11544,
    title="Abdication",
    keywords=[Kharmic],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Political Open:</b> Search your Fate deck for an Allegiance card, show it, and put it in your hand.<br><b>Political Open:</b> Discard a target Allegiance card in play. Refill this Province face-up."
The_Samurai_Caste_Divides = Event(
    card_id=11545,
    title="The Samurai Caste Divides",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open:</b> Permanently give your target Personality <b>Resilient</b>. If you have fewer Provinces than each other player, permanently give him <b>Conqueror </b>and refill this Province face-up."
The_Serpent_War = Event(
    card_id=11546,
    title="The Serpent War",
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
