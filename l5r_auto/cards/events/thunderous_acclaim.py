from __future__ import annotations

from l5r_auto.keywords import Festival, Kharmic
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Event

'You have the ability, "<b>Open:</b> Give a target face-up card in your Province Kharmic."<br><b>Open:</b> Put this Event into play.'
A_Vision_Imparted = Event(
    card_id=12265,
    title="A Vision Imparted",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'You have the ability, "<b>Open:</b> If you have fewer Provinces than one other player, then a number of times per turn equal to the difference <i>(now)</i>, you may refill one of your Provinces face-up."<br><b>Open:</b> If you have not resolved a Coronation Festival this game, put this Event into play.'
Coronation_Festival = Event(
    card_id=12266,
    title="Coronation Festival",
    keywords=[Kharmic, Festival],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'You have the ability, "<b>Battle:</b> If your current army is opposed, discard a card to draw a card."<br><b>Open:</b> Put this Event into play.'
Exodus_of_the_Spider = Event(
    card_id=12267,
    title="Exodus of the Spider",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
