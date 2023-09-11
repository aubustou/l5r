from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Alchemist,
    Cavalry,
    Duelist,
    Earth,
    Kensai,
    Magistrate,
    Monk,
    Reserve,
    Resilient,
    Samurai,
    Shugenja,
    Tattooed,
    Void,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Iaijutsu Battle, :bow::</b> Destroy a target enemy attachment with Force less than or equal to Futoro's Chi <i>(Spells have zero Force)</i>."
Mirumoto_Futoro = Personality(
    card_id=11574,
    title="Mirumoto Futoro",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Cavalry, Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Jaikei does not gain Addiction tokens.<br>Invest :g10:, :gstar:: Equip up to three Weapons to your Personalities, paying 4 less Gold each. You may target and bow a Shugenja. This Invest cost cannot be reduced."
Mirumoto_Jaikei = Personality(
    card_id=11575,
    title="Mirumoto Jaikei",
    force=3,
    chi=1,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[DragonClan],
    keywords=[Kensai, Reserve, Resilient, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br><b>Battle, :bow::</b> Melee Attack equal to Saiko's Force."
Mirumoto_Saiko = Personality(
    card_id=11576,
    title="Mirumoto Saiko",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Ginrao enters play for 1 less Gold if your Allegiance is Progressive or you are a Crane Clan player. Ginrao also enters play for 2 less Gold if you do not control another Ginrao or you took a Kharmic action this turn."
Tamori_Ginrao = Personality(
    card_id=11577,
    title="Tamori Ginrao",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Earth, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open, :bow::</b> Create a <b>Potion</b> Item with the ability, \"<b>Engage:</b> Destroy this Item to give this Personality +2F, the ability, '<b>Battle:</b> Fear 3', and a -1C <b>Addiction</b> token\" and attach it to your target Personality without a Potion Item."
Tamori_Wataru = Personality(
    card_id=11578,
    title="Tamori Wataru",
    force=1,
    chi=5,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[DragonClan],
    keywords=[Alchemist, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Void Engage:</b> You may give Shao +1F, or you may target an enemy Personality with higher printed Force and give him a Force penalty, and Shao a bonus, equal to the difference between their printed force."
Togashi_Shao = Personality(
    card_id=11579,
    title="Togashi Shao",
    force=2,
    chi=4,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Resilient, Monk, Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
