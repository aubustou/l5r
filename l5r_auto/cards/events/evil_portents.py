from __future__ import annotations

from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Event

"<b>Open:</b> Dark times are coming. Personalities with 3 or more Personal Honor have -1F. Personalities with 0 Personal Honor have +1F."
Battle_of_the_First_Seal = Event(
    card_id=12421,
    title="Battle of the First Seal",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Invest :g2::</b> The Event may be Unique.<br><b>Political Open:</b> Search your Dynasty deck for a non-Unique Event not named Ominous Revelation and refill this Province with it, face-up."
Ominous_Revelation = Event(
    card_id=12422,
    title="Ominous Revelation",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Ninja Open, :g2::</b> You may target and bow a Spell. Search your Fate deck for a Ninja Strategy, show it, and put it in your hand. Lose 2 Honor."
War_of_the_Spirit_Realms = Event(
    card_id=12423,
    title="War of the Spirit Realms",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
