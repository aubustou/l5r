from __future__ import annotations

from l5r_auto.cards.personalities.common import Personality
from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Air,
    Artisan,
    ClanChampion,
    Courtier,
    Duelist,
    Experienced,
    Governor,
    Loyal,
    Magistrate,
    Samurai,
    Scout,
    Seductress,
    Shugenja,
    SoulOf,
    TheSmilingBlade,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

Asahina_Umeko = Personality(
    id=11155,
    title="Asahina Umeko",
    force=0,
    chi=4,
    honor_requirement=0,
    personal_honor=2,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Air, Shugenja, SoulOf("Asahina Kimita")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Kinta = Personality(
    id=11156,
    title="Daidoji Kinta",
    force=2,
    chi=2,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Samurai, SoulOf("Daidoji Gudeta")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Tanshi = Personality(
    id=11157,
    title="Daidoji Tanshi",
    force=3,
    chi=3,
    honor_requirement=5,
    personal_honor=2,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Daidoji_Ujirou = Personality(
    id=11158,
    title="Daidoji Ujirou",
    force=3,
    chi=3,
    honor_requirement=3,
    personal_honor=3,
    gold_cost=7,
    clan=[CraneClan],
    keywords=[Samurai, Scout, SoulOf("Daidoji Gempachi")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Etsuki = Personality(
    id=11159,
    title="Doji Etsuki",
    force=3,
    chi=4,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=6,
    clan=[CraneClan],
    keywords=[Governor, Magistrate, Samurai, SoulOf("Doji Numata")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Katata = Personality(
    id=11160,
    title="Doji Katata",
    force=0,
    chi=1,
    honor_requirement=8,
    personal_honor=3,
    gold_cost=8,
    clan=[CraneClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Makoto_the_Smiling_Blade_Experienced = Personality(
    id=11161,
    title="Doji Makoto, the Smiling Blade",
    force=3,
    chi=6,
    honor_requirement=10,
    personal_honor=5,
    gold_cost=10,
    clan=[CraneClan],
    keywords=[
        Duelist,
        Loyal,
        Unique,
        ClanChampion,
        Courtier,
        Experienced("1"),
        Samurai,
        TheSmilingBlade,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Shirarou = Personality(
    id=11162,
    title="Doji Shirarou",
    force=2,
    chi=3,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Artisan, Samurai, SoulOf("Doji Bukita")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Doji_Soeka = Personality(
    id=11163,
    title="Doji Soeka",
    force=2,
    chi=4,
    honor_requirement=6,
    personal_honor=3,
    gold_cost=7,
    clan=[CraneClan],
    keywords=[Courtier, Magistrate, Seductress, SoulOf("Doji Nenkai")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Amiki = Personality(
    id=11164,
    title="Kakita Amiki",
    force=1,
    chi=3,
    honor_requirement=5,
    personal_honor=3,
    gold_cost=5,
    clan=[CraneClan],
    keywords=[Duelist, Courtier, Samurai, SoulOf("Kakita Funaki")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
Kakita_Ibara = Personality(
    id=11165,
    title="Kakita Ibara",
    force=3,
    chi=3,
    honor_requirement=0,
    personal_honor=1,
    gold_cost=4,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, IvoryEdition, ModernEdition],
)
