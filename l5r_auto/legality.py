from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Legality:
    pass


@dataclass(kw_only=True)
class Imperial(Legality):
    pass


@dataclass(kw_only=True)
class Jade(Legality):
    pass


@dataclass(kw_only=True)
class Gold(Legality):
    pass


@dataclass(kw_only=True)
class Diamond(Legality):
    pass


@dataclass(kw_only=True)
class Lotus(Legality):
    pass


@dataclass(kw_only=True)
class Samurai(Legality):
    pass


@dataclass(kw_only=True)
class Celestial(Legality):
    pass


@dataclass(kw_only=True)
class Emperor(Legality):
    pass


@dataclass(kw_only=True)
class Ivory(Legality):
    pass


@dataclass(kw_only=True)
class TwentyFestivals(Legality):
    pass


@dataclass(kw_only=True)
class Onyx(Legality):
    pass


@dataclass(kw_only=True)
class Modern(Legality):
    pass
