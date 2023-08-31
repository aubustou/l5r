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
