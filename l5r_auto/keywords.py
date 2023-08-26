from __future__ import annotations

from dataclasses import dataclass, field
from l5r_auto.card import Card, Keyword


@dataclass(kw_only=True)
class Cavalry(Keyword):
    pass


@dataclass(kw_only=True)
class Samurai(Keyword):
    pass
