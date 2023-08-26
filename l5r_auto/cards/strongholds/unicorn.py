from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Ability, Card
from l5r_auto.cards.followers.common import Follower
from l5r_auto.cards.personalities.common import Personality, PersonalityEntity

from l5r_auto.cards.strongholds.common import Stronghold
from l5r_auto.clans import Unicorn, Clan


# Northern Provinces of the Moto


@dataclass(kw_only=True)
class ProduceGoldForCavalry(Ability):
    """w: When paying for a Cavalry Follower, produce 7 Gold that may only pay for it."""

    base_gold_amount: int
    gold_amount: int

    def on_pay(self, type_: Type[Card], keywords: list[str]) -> int:
        if type_ is Follower and "Cavalry" in keywords:
            return self.gold_amount
        else:
            return self.base_gold_amount


@dataclass(kw_only=True)
class NorthernProvincesBattleAbility(Ability):
    """Repeatable Tireless Battle: Target your two unbowed Cavalry Personalities that this action has not targeted this turn, one of whom may be at any location. Switch their locations."""

    repeatable: bool = True
    tireless: bool = True
    battle: bool = True

    targeted_this_turn: list[PersonalityEntity] = field(
        default_factory=list, init=False
    )

    def perform_action(self, cavalry1: PersonalityEntity, cavalry2: PersonalityEntity):
        if (
            cavalry1 not in self.targeted_this_turn
            and cavalry2 not in self.targeted_this_turn
        ):
            cavalry1.location, cavalry2.location = cavalry2.location, cavalry1.location
            self.targeted_this_turn.extend([cavalry1, cavalry2])


NorthernProvincesOfTheMoto = Stronghold(
    id=5625,
    title="Northern Provinces of the Moto",
    province_strength=7,
    gold_production=5,
    starting_honor=4,
    clan=Unicorn,
    abilities=[
        ProduceGoldForCavalry(base_gold_amount=7, gold_amount=7),
        NorthernProvincesBattleAbility(),
    ],
)
