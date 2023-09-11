from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, Unaligned
from l5r_auto.keywords import (
    Actor,
    Duelist,
    Fire,
    Kensai,
    Monk,
    Ronin,
    Samurai,
    Shugenja,
    SoulOf,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"After you Recruit Dainiko, give her four +1F <b>Fire</b> tokens."
Dainiko = Personality(
    card_id=11229,
    title="Dainiko",
    force=0,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=0,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[Fire, Monk, Ronin, SoulOf("Nakadai")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i><i>(Duelists win tied duels versus non-Duelists. Kensai may attach two Weapons, as long as neither is Two-Handed.)</i></i>"
Horobei = Personality(
    card_id=11230,
    title="Horobei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[Unaligned],
    keywords=[Duelist, Kensai, Ronin, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open:</b> Myuken copies one keyword from your target Personality."
Myuken = Personality(
    card_id=11231,
    title="Myuken",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Actor, Ronin, SoulOf("Kyogen")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Battle, :bow::</b> Ranged Attack with strength equal to Shinzai's Chi."
Yotsu_Shinzai = Personality(
    card_id=11232,
    title="Yotsu Shinzai",
    force=1,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Shugenja, SoulOf("Yotsu Seiki")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
