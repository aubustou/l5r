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

"<b>Battle, :bow::</b> Ranged 2 Attack. <i>(Destroy a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>"
Aikiren = Personality(
    card_id=11776,
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
"<i>(Duelists win tied duels versus non-Duelists. Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br><b>Iaijutsu Battle:</b> Oneiyara challenges a target enemy Personality. After the duel, Fear equal to Oneiyara's Force that targets the loser."
Oneiyara = Personality(
    card_id=11777,
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
"After Patairaku enters play, lose 3 Honor. <br><b>Battle, :g2::</b> Create a 1F <b>Goblin &#149; Nonhuman &#149; Pet &#149; Shadowlands</b> Follower and attach it to Patairaku."
Patairaku_no_Oni = Personality(
    card_id=11778,
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
"<i>(Shugenja may attach and cast Spells.)</i><br>Teshan Lobbies without bowing."
Seppun_Teshan = Personality(
    card_id=11779,
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
"Zenathaar will not join you if you control any Shadowlands Personalities. Your other Naga Personalities have +1PH. <br><b>Home Battle:</b> Move your target Naga Personality home."
Zenathaar = Personality(
    card_id=11780,
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
