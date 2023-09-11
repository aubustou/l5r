from __future__ import annotations

from l5r_auto.clans import PhoenixClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Destined,
    Earth,
    Fire,
    Resilient,
    Samurai,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Earth Open, :bow:, [*]:</b> Recruit a target Fortification in your discard pile <i>(attach it to any of your Provinces)</i>. Give its Province a +1 strength <b>Wall </b>token."
Agasha_Beiru = Personality(
    card_id=11592,
    title="Agasha Beiru",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Air Open, :bow::</b> If it is not your turn, target one of your Provinces. It is consecrated. Before the turn ends, if it hasn't been destroyed, gain 1 Honor."
Isawa_Kaisei = Personality(
    card_id=11593,
    title="Isawa Kaisei",
    force=0,
    chi=3,
    personal_honor=4,
    gold_cost=7,
    honor_requirement=6,
    clan=[PhoenixClan],
    keywords=[Cavalry, Destined, Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
'Orinoko enters play for 1 less Gold if your Allegiance is Traditionalist.<br>Invest :g10:: Give Orinoko three +1F/+1C tokens, then permanently give her <b>Conqueror</b> and the ability, "<b>Fire Battle:</b> Fear 5." This Invest cost cannot be reduced.'
Isawa_Orinoko = Personality(
    card_id=11594,
    title="Isawa Orinoko",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=None,
    clan=[PhoenixClan],
    keywords=[Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Fire Battle:</b> If Waiko has a Fire Spell, Ranged 2 Attack."
Isawa_Waiko = Personality(
    card_id=11595,
    title="Isawa Waiko",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Resilient, Fire, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Interrupt:</b> After you Recruit Tuoko, create a 0F/2C/2PH Phoenix <b>Clan &#149; Void &#149; Shugenja</b> Personality."
Shiba_Tuoko = Personality(
    card_id=11596,
    title="Shiba Tuoko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Resilient, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Melee 2 Attack, or 3 if you took a Kharmic action this turn."
Shiba_Yinfuo = Personality(
    card_id=11597,
    title="Shiba Yinfuo",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[PhoenixClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
