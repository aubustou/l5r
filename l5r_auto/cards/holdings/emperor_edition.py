from __future__ import annotations

from dataclasses import dataclass
from typing import Type

from l5r_auto.cards import Entity
from l5r_auto.clans import (
    Clan,
    CrabClan,
    CraneClan,
    DragonClan,
    LionClan,
    MantisClan,
    PhoenixClan,
    ScorpionClan,
    SpiderClan,
    UnicornClan,
)
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
from l5r_auto.play import Game
from l5r_auto.player import Player

from ...abilities import ProduceGold
from .common import Holding


@dataclass(repr=False, kw_only=True)
class ClanHoldingAbility(ProduceGold):
    """Bow: Produce 2 Gold, or 3 Gold if you are a {clan} Clan player."""

    clan: Type[Clan]

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        if player.clan == self.clan:
            return 3
        else:
            return 2


"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Lion Clan player."
Copper_Mine = Holding(
    card_id=1497,
    title="Copper Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[ClanHoldingAbility(clan=LionClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Interrupt:</b> If it is the Action Phase, reduce one of the Honor gains or losses from the action to 0. Destroy this Holding."
Deeds_and_Words = Holding(
    card_id=1914,
    title="Deeds and Words",
    gold_cost=2,
    traits=[],
    abilities=[ClanHoldingAbility(clan=CrabClan)],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Limited:</b> Discard a face-up card from one of your Provinces. Refill the Province with your target discarded <i>(not dead)</i> Personality. Destroy this Holding."
Family_Library = Holding(
    card_id=2463,
    title="Family Library",
    gold_cost=2,
    keywords=[Library],
    traits=[],
    abilities=[ProduceGold(base_gold_amount=2)],
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
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Scorpion Clan player."
Geisha_House = Holding(
    card_id=2784,
    title="Geisha House",
    gold_cost=2,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[ClanHoldingAbility(clan=ScorpionClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Dragon Clan player."
Gold_Mine = Holding(
    card_id=2867,
    title="Gold Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[ClanHoldingAbility(clan=DragonClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crab Clan player."
Iron_Mine = Holding(
    card_id=3808,
    title="Iron Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[ClanHoldingAbility(clan=CrabClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Mantis Clan player."
Kobune_Port = Holding(
    card_id=4496,
    title="Kobune Port",
    gold_cost=2,
    keywords=[Port],
    traits=[],
    abilities=[ClanHoldingAbility(clan=MantisClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Crane Clan player."
Marketplace = Holding(
    card_id=4840,
    title="Marketplace",
    gold_cost=2,
    keywords=[Market],
    traits=[],
    abilities=[ClanHoldingAbility(clan=CraneClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Spider Clan player."
Shinomen_Marsh = Holding(
    card_id=6984,
    title="Shinomen Marsh",
    gold_cost=2,
    keywords=[Swamp],
    traits=[],
    abilities=[ClanHoldingAbility(clan=SpiderClan)],
    legality=[
        IvoryEdition,
        TwentyFestivalsEdition,
        EmperorEdition,
        CelestialEdition,
        SamuraiEdition,
        ModernEdition,
        ModernEdition,
    ],
    gold_production="2*",
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
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Phoenix Clan player."
Silver_Mine = Holding(
    card_id=7266,
    title="Silver Mine",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[ClanHoldingAbility(clan=PhoenixClan)],
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
    gold_production="2*",
)
"<b>:bow::</b> Produce 2 Gold, or 3 Gold if you are a Unicorn Clan player."
Stables = Holding(
    card_id=7443,
    title="Stables",
    gold_cost=2,
    keywords=[Stables],
    traits=[],
    abilities=[ClanHoldingAbility(clan=UnicornClan)],
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
    gold_production="2*",
)
