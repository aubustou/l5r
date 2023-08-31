from __future__ import annotations

from dataclasses import dataclass, field
from typing import Type
from l5r_auto.card import Ability, Card


from l5r_auto.cards.strongholds.common import Stronghold
from l5r_auto.clans import Mantis
from l5r_auto.keywords import Port, Naval
from l5r_auto.legality import Diamond, Gold
from l5r_auto.player import Player


@dataclass(kw_only=True)
class KyudenGoteiBattleAbility(Ability):
    """Battle: Once per battle, bow your target performing Naval card to take two additional Battle actions."""

    battle: bool = True

    def perform_action(self, player: Player, card: Card):
        if Naval in card.keywords:
            player.battle_actions += 2


@dataclass(kw_only=True)
class KyudenGoteiAbility(Ability):
    def at_start(self, player: Player):
        player.available_abilities.append(KyudenGoteiBattleAbility())


KyudenGotei = Stronghold(
    id=4636,
    title="Kyuden Gotei",
    province_strength=7,
    gold_production=4,
    starting_family_honor=3,
    clan=Mantis,
    keywords=[Port],
    abilities=[KyudenGoteiAbility()],
    legality=[Gold, Diamond],
)
