from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Clan:
    id: int


@dataclass
class BrotherhoodOfShinsei(Clan):
    id: int = 1
    name: str = "Brotherhood of Shinsei"


@dataclass
class Crab(Clan):
    id: int = 2
    name: str = "Crab"


@dataclass
class Crane(Clan):
    id: int = 3
    name: str = "Crane"


@dataclass
class Dragon(Clan):
    id: int = 4
    name: str = "Dragon"


@dataclass
class Lion(Clan):
    id: int = 5
    name: str = "Lion"


@dataclass
class Mantis(Clan):
    id: int = 6
    name: str = "Mantis"


@dataclass
class Naga(Clan):
    id: int = 7
    name: str = "Naga"


@dataclass
class Phoenix(Clan):
    id: int = 8
    name: str = "Phoenix"


@dataclass
class Ratling(Clan):
    id: int = 9
    name: str = "Ratling"


@dataclass
class Scorpion(Clan):
    id: int = 10
    name: str = "Scorpion"


@dataclass
class Shadowlands(Clan):
    id: int = 11
    name: str = "Shadowlands"


@dataclass
class Spider(Clan):
    id: int = 12
    name: str = "Spider"


@dataclass
class Spirit(Clan):
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
class Unicorn(Clan):
    id: int = 16
    name: str = "Unicorn"
