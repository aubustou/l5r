from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from l5r_auto.abilities import Ability
from l5r_auto.cards.followers.common import Follower
from l5r_auto.cards.personalities.common import PersonalityEntity
from l5r_auto.cards.strongholds.common import Stronghold
from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import Cavalry
from l5r_auto.legality import DiamondEdition, GoldEdition, JadeEdition
from l5r_auto.utils import is_entity_of_type

if TYPE_CHECKING:
    from l5r_auto.cards import Entity
    from l5r_auto.play import Game
    from l5r_auto.player import Player

# Northern Provinces of the Moto


@dataclass(repr=False, kw_only=True)
class ProduceGoldForCavalry(Ability):
    """w: When paying for a Cavalry Follower, produce 7 Gold that may only pay for it."""

    base_gold_amount: int
    gold_amount: int

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        if is_entity_of_type(entity, Follower) and Cavalry in entity.keywords:
            return self.gold_amount
        else:
            return self.base_gold_amount


@dataclass(repr=False, kw_only=True)
class NorthernProvincesBattleAbility(Ability):
    """Repeatable Tireless Battle: Target your two unbowed Cavalry Personalities that this action has not targeted this turn, one of whom may be at any location. Switch their locations."""

    repeatable: bool = True
    tireless: bool = True
    battle: bool = True

    targeted_this_turn: list[PersonalityEntity] = field(
        default_factory=list, init=False
    )

    def gather_legal_target_entities(
        self, game: Game, active_player: Player
    ) -> list[PersonalityEntity]:
        return [
            x
            for x in active_player.play_area
            if is_entity_of_type(x, PersonalityEntity)
            and Cavalry in x.keywords
            and not x.bowed
            and x not in self.targeted_this_turn
        ]

    def get_effect(
        self,
        game: Game,
        active_player: Player,
        targets: tuple[PersonalityEntity, PersonalityEntity],
    ):
        one_cavalry, two_cavalry = targets
        one_location = one_cavalry.location
        two_location = two_cavalry.location
        one_cavalry.move_to(two_location)
        two_cavalry.move_to(one_location)

    def pay_cost(self, game: Game, entity: PersonalityEntity) -> bool:
        return True


NorthernProvincesOfTheMoto = Stronghold(
    card_id=5625,
    title="Northern Provinces of the Moto",
    province_strength=7,
    gold_production="5",
    starting_family_honor=4,
    clan=[UnicornClan],
    abilities=[
        ProduceGoldForCavalry(base_gold_amount=5, gold_amount=7),
        NorthernProvincesBattleAbility(),
    ],
    legality=[DiamondEdition, JadeEdition, GoldEdition],
)
