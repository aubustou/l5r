from __future__ import annotations

from l5r_auto.clans import MantisClan
from l5r_auto.keywords import (
    Earth,
    Experienced,
    Jade,
    Kolat,
    LadyOfTheSun,
    Magistrate,
    Naval,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    Thunder,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

'<i>(Shugenja may attach and cast Spells.)</i><br><b>Interrupt:</b> After you Recruit Beiko, create a 5F/2C/3PH Mantis <b>Clan &#149; Bear &#149; Nonhuman &#149; Spirit</b> Personality with the trait, "Has -2F while attacking" and the ability, "<b>Battle:</b> Fear 4."'
Kitsune_Beiko = Personality(
    card_id=11752,
    title="Kitsune Beiko",
    force=0,
    chi=1,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once a turn, the attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br>Raiko has +1F/+1C while she has an Air, Fire, or Thunder Spell."
Moshi_Raiko = Personality(
    card_id=11753,
    title="Moshi Raiko",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, LadyOfTheSun, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action.)</i> <br><b>Battle, :bow::</b> Ranged 2 Attack."
Tsuruchi_Hikari = Personality(
    card_id=11754,
    title="Tsuruchi Hikari",
    force=2,
    chi=1,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Jade Battle, :bow::</b> Ranged 4 Attack. Straighten Yashiro if the target was Shadowlands."
Tsuruchi_Yashiro_Defender_of_the_Obsidian_Blades_Experienced = Personality(
    card_id=11755,
    title="Tsuruchi Yashiro, Defender of the Obsidian Blades",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Unique, Experienced("1"), Jade, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Invest :g2:, or [0] if another player is Phoenix Clan: Permanently give Shotsuo <b>Conqueror</b>. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once. A Conqueror's unit doesn't bow after battle.)</i>"
Yoritomo_Shotsuo = Personality(
    card_id=11756,
    title="Yoritomo Shotsuo",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Tireless Open:</b> Dishonor Yusuke to straighten him.<br><b>:bow::</b> Produce 2 Gold."
Yoritomo_Yusuke = Personality(
    card_id=11757,
    title="Yoritomo Yusuke",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kolat, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
