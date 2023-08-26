"""Title
Moto Chagatai
Type
Personality
F/C
4 3
HR/Cost/PH
- 8 1
Clan
Unicorn
Keywords
Cavalry • Samurai • Soul of Moto Soro • Unicorn Clan
Text
Chagatai is not destroyed for having 0 Chi unless his Chi is 0 after all penalties that last until your turn ends wear off."""

from __future__ import annotations

from dataclasses import dataclass, field

from l5r_auto.card import Ability, Card
from l5r_auto.cards.personalities.common import Personality, PersonalityEntity, SoulOf
from l5r_auto.keywords import Cavalry, Samurai


class MotoChagataiAbility(Ability):
    """Chagatai is not destroyed for having 0 Chi unless his Chi is 0 after all penalties that last until your turn ends wear off."""

    def check_chi(self, personality: PersonalityEntity):
        if isinstance(personality, MotoChagatai) and personality.chi == 0:
            return False
        else:
            return True


MotoChagatai = Personality(
    id=5299,
    title="Moto Chagatai",
    force=4,
    chi=3,
    honor_requirement=None,
    personal_honor=8,
    gold_cost=1,
    clan="Unicorn",
    keywords=[Cavalry, Samurai, SoulOf("Moto Soro")],
    traits=[],
    abilities=[],
)
