from __future__ import annotations

from l5r_auto.clans import NagaFaction, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import (
    Air,
    Courtier,
    Duelist,
    HiddenGuard,
    Imperial,
    Kensai,
    Naga,
    Nonhuman,
    Oni,
    Ronin,
    Savior,
    Scout,
    Shadowlands,
    Shugenja,
    WarriorOfTheBrightEye,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

Aikiren = Personality(
    id=11776,
    title="Aikiren",
    force=0,
    chi=1,
    personal_honor=0,
    gold_cost=2,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Ronin],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
Oneiyara = Personality(
    id=11777,
    title="Oneiyara",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Duelist, Kensai, Ronin],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Patairaku_no_Oni = Personality(
    id=11778,
    title="Patairaku no Oni",
    force=5,
    chi=3,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Seppun_Teshan = Personality(
    id=11779,
    title="Seppun Teshan",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=8,
    clan=[Unaligned],
    keywords=[Air, Courtier, HiddenGuard, Imperial, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Zenathaar = Personality(
    id=11780,
    title="Zenathaar",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[Unaligned, NagaFaction],
    keywords=[Naga, Nonhuman, Savior, Scout, WarriorOfTheBrightEye],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
