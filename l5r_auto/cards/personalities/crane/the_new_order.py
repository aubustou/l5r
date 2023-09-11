from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Cavalry,
    Conqueror,
    Courtier,
    Duelist,
    Kensai,
    LoveLetter,
    Magistrate,
    Orator,
    Samurai,
    ScourgeOfDarkness,
    Scout,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Engage:</b> If Nozomi moved this battle, give her <b>Naval</b>. <br><b>Battle:</b> Fear equal to Nozomi's Force, or 2 if she is Naval."
Daidoji_Nozomi = Personality(
    card_id=11891,
    title="Daidoji Nozomi",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Cavalry, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Tomomi enters play for 1 less Gold if you are a Mantis Clan player."
Daidoji_Tomomi = Personality(
    card_id=11890,
    title="Daidoji Tomomi",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Conqueror, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Yurei will not enter play if you control a Fallen or Shadowlands Personality. Yurei has +1F for each Personality with 0 Personal Honor opposing him.<br><b>Battle:</b> Fear equal to Yurei's Force."
Daidoji_Yurei = Personality(
    card_id=11895,
    title="Daidoji Yurei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=9,
    clan=[CraneClan],
    keywords=[Duelist, Samurai, ScourgeOfDarkness],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Doji_Shimada = Personality(
    card_id=11893,
    title="Doji Shimada",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Courtesy: After you Recruit Takato, gain 1 Honor. <i>(Courtesy traits do not take effect if you went first.)</i><br><b>Interrupt:</b> After you Recruit Takato, discard a card to make a target player discard a random card. Each of you may put the other's card in your hand."
Doji_Takato_the_Manipulator = Personality(
    card_id=11892,
    title="Doji Takato, the Manipulator",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, LoveLetter, Orator],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Daitsu has +1C while you control Kakita Shinichi. Daitsu will only attach one Weapon.<br><b>Unstoppable Battle, :bow::</b> Melee 2 Attack. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Kakita_Daitsu = Personality(
    card_id=11894,
    title="Kakita Daitsu",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Duelist, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
