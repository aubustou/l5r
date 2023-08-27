from __future__ import annotations

from dataclasses import dataclass, field

from l5r_auto.card import Ability, Card, Trait
from l5r_auto.cards.personalities.common import Personality, PersonalityEntity, SoulOf
from l5r_auto.cards.regions.common import Region
from l5r_auto.clans import Unicorn
from l5r_auto.keywords import Baraunghar, Bushi, Cavalry, Explorer, Samurai
from l5r_auto.locations import Battlefield
from l5r_auto.phases import BattlePhase
from l5r_auto.rules import pay_cost


class MotoChagataiAbility(Ability):
    """Chagatai is not destroyed for having 0 Chi unless his Chi is 0 after all penalties that last until your turn ends wear off."""

    def prevent_zero_chi(self, personality: PersonalityEntity):
        # TODO: Implement this
        pass


MotoChagatai = Personality(
    id=5299,
    title="Moto Chagatai",
    force=4,
    chi=3,
    honor_requirement=None,
    personal_honor=8,
    gold_cost=1,
    clan=[Unicorn],
    keywords=[Cavalry, Samurai, SoulOf("Moto Soro")],
    traits=[],
    abilities=[MotoChagataiAbility()],
)


class MotoKaduAbility(Ability):
    """Battle, w: Destroy Kadu-kai to destroy a target enemy Personality with equal or lower Force."""

    battle: bool = True

    def destroy_enemy(self, kadu: PersonalityEntity, enemy: PersonalityEntity):
        if pay_cost(kadu.bow):
            kadu.destroy()
            enemy.target()
            if enemy.force <= kadu.force:
                enemy.destroy()


MotoKadu = Personality(
    id=5339,
    title="Moto Kadu",
    force=3,
    chi=2,
    honor_requirement=4,
    personal_honor=8,
    gold_cost=2,
    clan=[Unicorn],
    keywords=[Cavalry, Samurai, SoulOf("Moto Toyotomi")],
    traits=[],
    abilities=[MotoKaduAbility()],
)


class ShinjoReizoTerrain(Ability):
    """Reizo has +2F while a Terrain is in play at his battlefield.
    Reizo has +2F while any Regions are attached to his battlefield's province.
    """

    def modify_force(self, reizo: PersonalityEntity):
        if reizo.location is Battlefield:
            if getattr(reizo.location, "terrain", None) is not None:
                reizo.force = reizo.force + 2
            if (
                province := getattr(reizo.location, "province", None)
            ) is not None and any(isinstance(x, Region) for x in province.attachments):
                reizo.force = reizo.force + 2


ShinjoReizo = Personality(
    id=6924,
    title="Shinjo Reizo",
    force=1,
    chi=2,
    honor_requirement=0,
    personal_honor=5,
    gold_cost=2,
    clan=[Unicorn],
    keywords=[Cavalry, Explorer, Samurai, SoulOf("Shinjo Rojin")],
    traits=[],
    abilities=[],
)

"""Title
Shinjo Xushen
Type
Personality
F/C
3 3
HR/Cost/PH
- 8 1
Clan
Unicorn
Keywords
Cavalry • Baraunghar • Bushi • Unicorn Clan
Text
During an Attack Phase, if Xushen assigned during its Infantry Maneuvers Segment, he has +1F and Ranged Attacks from actions he performs have +1 strength.
Battle: Bow Xushen: Ranged 3 Attack."""


class ShinjoXushenTrait(Trait):
    """During an Attack Phase, if Xushen assigned during its Infantry Maneuvers Segment, he has +1F and Ranged Attacks from actions he performs have +1 strength."""

    def modify_force(self, xushen: PersonalityEntity):
        if xushen.location is Battlefield:
            if xushen.game.current_phase is BattlePhase:
                if xushen.location.current_segment == "Infantry Maneuvers":
                    xushen.force = xushen.force + 1
                    xushen.ranged_attack_strength = xushen.ranged_attack_strength + 1


ShinjoXushen = Personality(
    id=6925,
    title="Shinjo Xushen",
    force=3,
    chi=3,
    honor_requirement=None,
    personal_honor=8,
    gold_cost=1,
    clan=[Unicorn],
    keywords=[Cavalry, Baraunghar, Bushi],
    traits=[],
    abilities=[],
)
