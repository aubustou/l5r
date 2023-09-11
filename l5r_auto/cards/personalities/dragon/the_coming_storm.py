from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import (
    BlessedByBenten,
    Cavalry,
    Courtier,
    Earth,
    Kensai,
    Magistrate,
    Monk,
    Samurai,
    Shugenja,
    Tattooed,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Political Battle, :bow::</b> Dishonor a target enemy Personality and give him -2F. If this targeted a Crab Clan Personality, you may target another Personality and give him -2F."
Kitsuki_Kira = Personality(
    card_id=11740,
    title="Kitsuki Kira",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Courtier, Magistrate],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle. Kensai may attach two Weapons, as long as neither is Two-Handed.)</i>"
Mirumoto_Reiji = Personality(
    card_id=11741,
    title="Mirumoto Reiji",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Cavalry, Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Takanori has +1C while he has a Weapon.<br><b>Battle:</b> Fear equal to Takanori's Chi."
Mirumoto_Takanori = Personality(
    card_id=11742,
    title="Mirumoto Takanori",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br>Your Provinces with one or more Fortifications attached have +1 strength."
Tamori_Junya = Personality(
    card_id=11743,
    title="Tamori Junya",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Battle:</b> Bow or destroy Touya's target Spell to reduce a target enemy Follower or Personality's Force by the Spell's Focus Value. If the Spell was Earth, gain 1 Honor."
Tamori_Touya = Personality(
    card_id=11744,
    title="Tamori Touya",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[BlessedByBenten, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Destroy a target enemy attachment with Force less than or equal to Yayoi's Chi."
Togashi_Yayoi = Personality(
    card_id=11745,
    title="Togashi Yayoi",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=2,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, Tattooed],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
