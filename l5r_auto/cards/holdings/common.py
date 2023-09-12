from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Type

from l5r_auto.abilities import ProduceGold
from l5r_auto.cards import DynastyCard, Entity
from l5r_auto.legality import Legality
from l5r_auto.locations import Deck, Location

if TYPE_CHECKING:
    pass


@dataclass(repr=False, kw_only=True)
class Holding(DynastyCard):
    gold_cost: int = field(metadata={"is_written": True})
    gold_production: str | None = field(metadata={"is_written": True})

    def __post_init__(self, *args, **kwargs):
        self.entity_type = HoldingEntity

        super().__post_init__(*args, **kwargs)
        if self.gold_production and not any(
            isinstance(x, ProduceGold) for x in self.abilities
        ):
            self.abilities.append(ProduceGold(base_gold_amount=self.gold_production))


@dataclass(repr=False, kw_only=True)
class HoldingEntity(Entity, Holding):
    location: Type[Location] = Deck


def get_cards(legality: Type[Legality]) -> list[Holding]:
    from .. import get_cards as get_cards_

    return [x for x in get_cards_(Holding) if legality in x.legality]
