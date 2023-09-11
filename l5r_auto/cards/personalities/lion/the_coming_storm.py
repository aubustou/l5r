from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Cavalry,
    Commander,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    Tactician,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Battle:</b> Target one or two of your unbowed Personalities at another battlefield. If they would be opposed, move them to this battlefield."
Akodo_Iketsu = Personality(
    card_id=11746,
    title="Akodo Iketsu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Tactician, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"Keisuke's printed ability has <b>Tireless</b> while you control a Terrain or Crab Clan Personality at his battlefield.<br><b>Battle:</b> Straighten a target attachment."
Ikoma_Keisuke = Personality(
    card_id=11747,
    title="Ikoma Keisuke",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to the battle. You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action.)</i><br>Shungo has +1F, or +2F if the Defender is Spider Clan, while attacking."
Ikoma_Shungo = Personality(
    card_id=11748,
    title="Ikoma Shungo",
    force=2,
    chi=1,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Cavalry, Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br>Scorpion Clan players ignore Asato's Honor Requirement.<br><b>Home Water Battle, :bow::</b> Give a target enemy Follower or Personality -2F."
Kitsu_Asato = Personality(
    card_id=11749,
    title="Kitsu Asato",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Open, :bow::</b> Create a 2F/2C/3PH Lion <b>Clan &#149; Ancestor &#149; Samurai &#149; Spirit</b> Personality."
Kitsu_Leiko = Personality(
    card_id=11750,
    title="Kitsu Leiko",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :g3::</b> Create a 1F <b>Cat &#149; Nonhuman</b> Follower and attach it to your target Personality."
Matsu_Marii = Personality(
    card_id=11751,
    title="Matsu Marii",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
