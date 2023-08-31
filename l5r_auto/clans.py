from __future__ import annotations


class Clan:
    id: int
    name: str
    alternative: list[str] = []

    @classmethod
    def module_name(cls) -> str:
        return cls.name.lower().replace(" ", "_")


class BrotherhoodOfShinsei(Clan):
    id: int = 1
    name: str = "Brotherhood of Shinsei"
    alternative: list[str] = ["Brotherhood", "Monk"]


class CrabClan(Clan):
    id: int = 2
    name: str = "Crab"
    alternative: list[str] = ["Crab Clan"]


class CraneClan(Clan):
    id: int = 3
    name: str = "Crane"
    alternative: list[str] = ["Crane Clan"]


class DragonClan(Clan):
    id: int = 4
    name: str = "Dragon"
    alternative: list[str] = ["Dragon Clan"]


class LionClan(Clan):
    id: int = 5
    name: str = "Lion"
    alternative: list[str] = ["Lion Clan"]


class MantisClan(Clan):
    id: int = 6
    name: str = "Mantis"
    alternative: list[str] = ["Mantis Clan", "Yoritomo's Alliance"]


class NagaFaction(Clan):
    id: int = 7
    name: str = "Naga"


class PhoenixClan(Clan):
    id: int = 8
    name: str = "Phoenix"
    alternative: list[str] = ["Phoenix Clan"]


class RatlingFaction(Clan):
    id: int = 9
    name: str = "Ratling"
    alternative: list[str] = ["Rat", "Nezumi"]


class ScorpionClan(Clan):
    id: int = 10
    name: str = "Scorpion"
    alternative: list[str] = ["Scorpion Clan"]


class ShadowlandsFaction(Clan):
    id: int = 11
    name: str = "Shadowlands"
    alternative: list[str] = ["Shadowlands Horde"]


class SpiderClan(Clan):
    id: int = 12
    name: str = "Spider"
    alternative: list[str] = ["Spider Clan"]


class SpiritFaction(Clan):
    id: int = 13
    name: str = "Spirit"
    alternative: list[str] = ["Spirit Army"]


class ToturisArmy(Clan):
    id: int = 14
    name: str = "Toturi's Army"


class Unaligned(Clan):
    id: int = 15
    name: str = "Unaligned"


class UnicornClan(Clan):
    id: int = 16
    name: str = "Unicorn"
    alternative: list[str] = ["Unicorn Clan"]


class NinjaFaction(Clan):
    id: int = 17
    name: str = "Ninja"


clans = [
    BrotherhoodOfShinsei,
    CrabClan,
    CraneClan,
    DragonClan,
    LionClan,
    MantisClan,
    NagaFaction,
    PhoenixClan,
    RatlingFaction,
    ScorpionClan,
    ShadowlandsFaction,
    SpiderClan,
    SpiritFaction,
    ToturisArmy,
    Unaligned,
    UnicornClan,
    NinjaFaction,
]
