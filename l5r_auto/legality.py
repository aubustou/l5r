from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Legality:
    pass


@dataclass(kw_only=True)
class ImperialEdition(Legality):
    pass


@dataclass(kw_only=True)
class JadeEdition(Legality):
    pass


@dataclass(kw_only=True)
class GoldEdition(Legality):
    pass


@dataclass(kw_only=True)
class DiamondEdition(Legality):
    pass


@dataclass(kw_only=True)
class LotusEdition(Legality):
    pass


@dataclass(kw_only=True)
class SamuraiEdition(Legality):
    pass


@dataclass(kw_only=True)
class CelestialEdition(Legality):
    pass


@dataclass(kw_only=True)
class EmperorEdition(Legality):
    pass


@dataclass(kw_only=True)
class IvoryEdition(Legality):
    pass


@dataclass(kw_only=True)
class TwentyFestivalsEdition(Legality):
    pass


@dataclass(kw_only=True)
class OnyxEdition(Legality):
    pass


@dataclass(kw_only=True)
class ModernEdition(Legality):
    pass
