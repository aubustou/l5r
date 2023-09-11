from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import Deathseeker, Resilient, Samurai, Scout, Shugenja, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Niito enters play for 1 less Gold if your Allegiance is Traditionalist.<br><b>Battle, :bow::</b> Target an enemy Personality with lower Personal Honor. Bow a number of target cards in his unit up to the difference in Personal Honor."
Akodo_Niito = Personality(
    card_id=11580,
    title="Akodo Niito",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Resilient, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>Invest :g10::</b> Search your discard pile and Dynasty deck for one or two copies of Akinari. Recruit them, ignoring costs. This Invest cost cannot be reduced."
Ikoma_Akinari = Personality(
    card_id=11581,
    title="Ikoma Akinari",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Genichi has <b>Resilient</b> while he opposes a Scorpion Clan Personality or you control a Terrain. <i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Battle, :bow::</b> Ranged 3 Attack."
Ikoma_Genichi = Personality(
    card_id=11582,
    title="Ikoma Genichi",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Increase your Honor gain from Proclaiming Junsuke to equal the number of Ancestors, up to 5, you control.<br><b>Home Battle, :bow::</b> Give your target defending Ancestor +2F."
Kitsu_Junsuke = Personality(
    card_id=11583,
    title="Kitsu Junsuke",
    force=1,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=2,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Water Dynasty/Open, :bow::</b> Straighten your target Fortification."
Kitsu_Watanabe = Personality(
    card_id=11584,
    title="Kitsu Watanabe",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Rishou cannot defend."
Matsu_Rishou = Personality(
    card_id=11585,
    title="Matsu Rishou",
    force=4,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=2,
    clan=[LionClan],
    keywords=[Deathseeker, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
