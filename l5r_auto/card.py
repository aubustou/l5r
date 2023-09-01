from __future__ import annotations

import uuid
from dataclasses import dataclass, field, fields
from typing import TYPE_CHECKING, Any, Type

from l5r_auto.keywords import Keyword

if TYPE_CHECKING:
    from .legality import Legality
    from .locations import DynastyDiscard, RemovedFromGame
    from .player import Entity


@dataclass(kw_only=True)
class Action:
    pass


@dataclass(kw_only=True)
class Ability(Action):
    repeatable: bool = False
    tireless: bool = False
    battle: bool = False


@dataclass(kw_only=True)
class Trait(Action):
    pass


@dataclass(kw_only=True)
class Card:
    card_id: int = field(metadata={"is_written": True})
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    title: str = field(metadata={"is_written": True})

    keywords: list[Type[Keyword]] = field(
        default_factory=list, metadata={"is_written": True}
    )
    legality: list[Type[Legality]] = field(
        default_factory=list, metadata={"is_written": True}
    )

    entity_type: Type[Entity] = field(init=False)

    def __post_init__(self):
        from .cards import CARDS

        CARDS.setdefault(self.__class__, {})[self.card_id] = self

    def written(self) -> dict[str, Any]:
        return {
            f.name: getattr(self, f.name)
            for f in fields(self)
            if f.metadata.get("is_written")
        }

    def __call__(self, *args: Any, **kwds: Any) -> Entity:
        # logging.debug(f"Creating {self.__class__.__name__} with {self.written()}")
        return self.entity_type(*args, **kwds, **self.written())

    def target(self):
        pass


@dataclass(kw_only=True)
class DynastyCard(Card):
    bowed: bool = False

    def destroy(self):
        self.location = DynastyDiscard

    def remove_from_game(self):
        self.location = RemovedFromGame


@dataclass(kw_only=True)
class FateCard(Card):
    gold_cost: int = field(metadata={"is_written": True})
    focus_value: int = field(metadata={"is_written": True})
