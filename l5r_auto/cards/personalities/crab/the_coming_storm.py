from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Courtier,
    Destined,
    Drunkard,
    Earth,
    Experienced,
    Hero,
    Jade,
    Magistrate,
    Merchant,
    Reserve,
    Samurai,
    Scout,
    Shugenja,
    Tactician,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Cannot attach Followers.<br><b>Battle:</b> <i>Zaiberu is belligerent.</i> Give a target enemy Follower or Personality -2F."
Hida_Zaiberu = Personality(
    card_id=11728,
    title="Hida Zaiberu",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Drunkard, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action.)</i><br>Maiko enters play for 1 less Gold if you are Lion Clan."
Hiruma_Maiko = Personality(
    card_id=11729,
    title="Hiruma Maiko",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Jade Battle:</b> Fear 3, or 5 if the target is Shadowlands, that may target a Personality with Followers."
Kuni_Shinoda_Advisor_to_the_Jade_Champion_Experienced_2 = Personality(
    card_id=11730,
    title="Kuni Shinoda, Advisor to the Jade Champion",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=9,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[
        Experienced("2"),
        Tactician,
        Unique,
        Earth,
        Hero,
        Jade,
        Magistrate,
        Scout,
        Shugenja,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Bow a target enemy card."
Toritaka_Isai = Personality(
    card_id=11731,
    title="Toritaka Isai",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
'Invest :g3:, or :g2: if another player is Dragon Clan: Permanently give your target Holding the ability, "<b>Economic Open, :bow::</b> A target player loses 1 Honor."'
Yasuki_Aitoko = Personality(
    card_id=11732,
    title="Yasuki Aitoko",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Destined, Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Economic Open, :bow::</b> Target a Personality with lower Personal Honor than printed. His controller may pay Gold equal to the difference plus 1. If he does not, he loses Honor equal to the difference."
Yasuki_Shairei = Personality(
    card_id=11733,
    title="Yasuki Shairei",
    force=0,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
