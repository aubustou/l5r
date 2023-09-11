from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    Commander,
    Courtier,
    Destined,
    Duelist,
    Earth,
    Kensai,
    LoveLetter,
    Monk,
    Samurai,
    Shugenja,
    Tattooed,
    Void,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Iaijutsu Battle:</b> Touya challenges a target enemy Personality. The winner creates Fear 4 targeting a <i>(legal)</i> card in the loser's unit <i>(there is no effect in a tie)</i>."
Mirumoto_Touya = Personality(
    card_id=11897,
    title="Mirumoto Touya",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card. Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br>Unless you are Spider Clan, discard a card after you Recruit Tsukino."
Mirumoto_Tsukino = Personality(
    card_id=11901,
    title="Mirumoto Tsukino",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=3,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Destined, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Iaijutsu Battle:</b> Yoritama challenges a target enemy Personality. Give the loser -3F. You may take an additional action if Yoritama has two Weapons."
Mirumoto_Yoritama = Personality(
    card_id=11896,
    title="Mirumoto Yoritama",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Political Open:</b> If it is another player's turn, target his unbowed Personality. Gain 1 Honor before the turn ends if the target did not attack you this turn."
Tamori_Chikyu = Personality(
    card_id=11898,
    title="Tamori Chikyu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Courtier, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Courtesy: After you Recruit Daiishu, gain 2 Honor and permanently give him <b>Naval</b>. <i>(Courtesy traits do not take effect if you went first. Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i>"
Tamori_Daiishu = Personality(
    card_id=11899,
    title="Tamori Daiishu",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=2,
    clan=[DragonClan],
    keywords=[Commander, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After you Recruit Doji Takato or Matsu Misato, bow Gozato.<br><b>Void Tireless Battle:</b> Bow your target unbowed Ring. Straighten Gozato or move him home."
Togashi_Gozato_the_Wise_Monk = Personality(
    card_id=11900,
    title="Togashi Gozato, the Wise Monk",
    force=3,
    chi=5,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[LoveLetter, Monk, Samurai, Tattooed, Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
