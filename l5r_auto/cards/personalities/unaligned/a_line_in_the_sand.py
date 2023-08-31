from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
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

Akenohoshi_the_Dancer = Personality(
    id=11610,
    title="Akenohoshi, the Dancer",
    force=0,
    chi=2,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=2,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, MaiMaster],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Harukaze_the_Confidant = Personality(
    id=11611,
    title="Harukaze, the Confidant",
    force=1,
    chi=3,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=3,
    clan=[Unaligned],
    keywords=[Artisan, Geisha],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Momiji_the_Madam = Personality(
    id=11612,
    title="Momiji, the Madam",
    force=1,
    chi=4,
    honor_requirement=None,
    personal_honor=2,
    gold_cost=4,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, Merchant],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Natsumi_the_Socialite = Personality(
    id=11613,
    title="Natsumi, the Socialite",
    force=0,
    chi=3,
    honor_requirement=None,
    personal_honor=3,
    gold_cost=4,
    clan=[Unaligned],
    keywords=[Artisan, Courtier, Geisha],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Oboro_the_Liar = Personality(
    id=11614,
    title="Oboro, the Liar",
    force=0,
    chi=2,
    honor_requirement=None,
    personal_honor=0,
    gold_cost=3,
    clan=[Unaligned],
    keywords=[Artisan, Geisha, Kolat, SilkenSect],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Suzune_the_Coy = Personality(
    id=11615,
    title="Suzune, the Coy",
    force=0,
    chi=2,
    honor_requirement=None,
    personal_honor=1,
    gold_cost=1,
    clan=[Unaligned],
    keywords=[Artisan, Geisha],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
