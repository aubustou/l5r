from __future__ import annotations

from l5r_auto.keywords import (
    GeishaHouse,
    Library,
    Market,
    Mine,
    Port,
    Stables,
    Swamp,
    Temple,
)
from l5r_auto.legality import (
    CelestialEdition,
    DiamondEdition,
    EmperorEdition,
    GoldEdition,
    ImperialEdition,
    IvoryEdition,
    JadeEdition,
    LotusEdition,
    ModernEdition,
    SamuraiEdition,
    TwentyFestivalsEdition,
)

from .common import Holding

"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Lion Clan player."
Copper_Mine = Holding(
    card_id=1497,
    title="Copper Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Interrupt:</b> If it is the Action Phase, reduce one of the Honor gains or losses from the action to 0. Destroy this Holding."
Deeds_and_Words = Holding(
    card_id=1914,
    title="Deeds and Words",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Limited:</b> Discard a face-up card from one of your Provinces. Refill the Province with your target discarded <i>(not dead)</i> Personality. Destroy this Holding."
Family_Library = Holding(
    card_id=2463,
    title="Family Library",
    gold_cost=2,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Scorpion Clan player."
Geisha_House = Holding(
    card_id=2784,
    title="Geisha House",
    gold_cost=2,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Dragon Clan player."
Gold_Mine = Holding(
    card_id=2867,
    title="Gold Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crab Clan player."
Iron_Mine = Holding(
    card_id=3808,
    title="Iron Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Mantis Clan player."
Kobune_Port = Holding(
    card_id=4496,
    title="Kobune Port",
    gold_cost=2,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        CelestialEdition,
        GoldEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crane Clan player."
Marketplace = Holding(
    card_id=4840,
    title="Marketplace",
    gold_cost=2,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Spider Clan player."
Shinomen_Marsh = Holding(
    card_id=6984,
    title="Shinomen Marsh",
    gold_cost=2,
    keywords=[Swamp],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Battle/Open:</b> Straighten a target attachment."
Shrine_to_Hachiman = Holding(
    card_id=7223,
    title="Shrine to Hachiman",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Phoenix Clan player."
Silver_Mine = Holding(
    card_id=7266,
    title="Silver Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Unicorn Clan player."
Stables = Holding(
    card_id=7443,
    title="Stables",
    gold_cost=2,
    keywords=[Stables],
    traits=[],
    abilities=[],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        LotusEdition,
        ImperialEdition,
        CelestialEdition,
        GoldEdition,
        JadeEdition,
        SamuraiEdition,
        DiamondEdition,
        ModernEdition,
        ModernEdition,
    ],
)
