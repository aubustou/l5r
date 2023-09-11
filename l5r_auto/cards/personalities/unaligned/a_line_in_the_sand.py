from __future__ import annotations

from l5r_auto.clans import Unaligned
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Geisha,
    Kolat,
    MaiMaster,
    Merchant,
    SilkenSect,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Open, :bow::</b> Give a target Human Personality +1F and <b>Conqueror</b>. <br><i>(A Conqueror's unit doesn't bow after battle.)</i>"
Akenohoshi_the_Dancer = Personality(
    card_id=11610,
    title="Akenohoshi, the Dancer",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, MaiMaster],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Invest :g6::</b> Show one or two non-Unique cards from your hand and/or Fate discard pile. Put them face-down under Harukaze and bow her.<br><b>Open, :bow:, :g2::</b> Put a card under Harukaze into your hand."
Harukaze_the_Confidant = Personality(
    card_id=11611,
    title="Harukaze, the Confidant",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Geisha],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action Recruits a Geisha <i>(including Momiji)</i> or a Geisha House from a Province, refill it face-up."
Momiji_the_Madam = Personality(
    card_id=11612,
    title="Momiji, the Madam",
    force=1,
    chi=4,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action shows a Battle Strategy in another player's hand, he may discard it. If he chooses not to, a target player gains or loses 1 Honor <i>(you must use this ability before the card is shown)</i>."
Natsumi_the_Socialite = Personality(
    card_id=11613,
    title="Natsumi, the Socialite",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Courtier, Geisha],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Invest :g3:<b>:</b> If you have not used the Invest trait of an Oboro this turn, shuffle all your other copies of Oboro in play and in your discard pile into your Dynasty Deck. Gain a <b>Conspiracy</b> token for each Oboro shuffled."
Oboro_the_Liar = Personality(
    card_id=11614,
    title="Oboro, the Liar",
    force=0,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, Kolat, SilkenSect],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Invest :g4::</b> Create a 3F/2C/1PH <b>Ronin &#149; Samurai &#149; Scout &#149; Yojimbo &#149; Resilient</b> Personality <i>(Once per game per card, a Resilient card does not die in battle resolution)</i>.<br><b>Open, :bow::</b> Straighten your target Human Scout or Yojimbo."
Suzune_the_Coy = Personality(
    card_id=11615,
    title="Suzune, the Coy",
    force=0,
    chi=2,
    personal_honor=1,
    gold_cost=1,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Artisan, Geisha],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
