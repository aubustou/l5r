from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Clan:
    id: int


@dataclass
class BrotherhoodOfShinsei(Clan):
    id: int = 1
    name: str = "Brotherhood of Shinsei"


@dataclass
class CrabClan(Clan):
    id: int = 2
    name: str = "Crab"


@dataclass
class CraneClan(Clan):
    id: int = 3
    name: str = "Crane"


@dataclass
class DragonClan(Clan):
    id: int = 4
    name: str = "Dragon"


@dataclass
class LionClan(Clan):
    id: int = 5
    name: str = "Lion"


@dataclass
class MantisClan(Clan):
    id: int = 6
    name: str = "Mantis"


@dataclass
class NagaFaction(Clan):
    id: int = 7
    name: str = "Naga"


@dataclass
class PhoenixClan(Clan):
    id: int = 8
    name: str = "Phoenix"


@dataclass
class RatlingFaction(Clan):
    id: int = 9
    name: str = "Ratling"


@dataclass
class ScorpionClan(Clan):
    id: int = 10
    name: str = "Scorpion"


@dataclass
class ShadowlandsFaction(Clan):
    id: int = 11
    name: str = "Shadowlands"


@dataclass
class SpiderClan(Clan):
    id: int = 12
    name: str = "Spider"


@dataclass
class SpiritFaction(Clan):
    id: int = 13
    name: str = "Spirit"


@dataclass
class ToturisArmy(Clan):
    id: int = 14
    name: str = "Toturi's Army"


@dataclass
class Unaligned(Clan):
    id: int = 15
    name: str = "Unaligned"


@dataclass
class UnicornClan(Clan):
    id: int = 16
    name: str = "Unicorn"


@dataclass
class NinjaFaction(Clan):
    id: int = 17
    name: str = "Ninja"
