from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Cavalry,
    Commander,
    Duelist,
    Experienced,
    Paragon,
    Samurai,
    ScionOfTheWind,
    Scout,
    Tactician,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Iaijutsu Battle:</b> Misaka challenges a target enemy Personality. The winner may target and give Reserve to a Personality in a Province, and if the winner was the challenged in the duel and defending, give that Reserve Personality -5GC."
Akodo_Misaka = Personality(
    card_id=12458,
    title="Akodo Misaka",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear equal to the number of attacking units in Morita's army, which may target a Personality with Followers if you control a Terrain."
Ikoma_Morita = Personality(
    card_id=12459,
    title="Ikoma Morita",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists. Battle: Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i> <br>After Akio uses her rulebook Tactical Advantage ability, give her a Chi bonus equal to half the Focus Value of the card discarded for it, rounded up."
Matsu_Akio = Personality(
    card_id=12460,
    title="Matsu Akio",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Duelist, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Battle:</b> Straighten Takeuchi's target Follower. If it is a Cat with higher Force than an opposing bowed Follower or Personality, the Cat may use its abilities an additional time this turn."
Matsu_Takeuchi = Personality(
    card_id=12461,
    title="Matsu Takeuchi",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Cavalry, Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"While attacking, Tayuko has +2F and +1F for each each Honor action you have resolved <i>(this turn)</i>.<br><b>Battle:</b> Move home a target enemy defending Personality with lower Personal Honor. If the target has fewer attachments, gain 1 Honor."
Matsu_Tayuko_Experienced = Personality(
    card_id=12462,
    title="Matsu Tayuko",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=8,
    clan=[LionClan],
    keywords=[Experienced("1"), Paragon, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Give Yamamura's target Nonhuman Follower a Force bonus equal to Yamamura's Force or the Force of any bowed enemy Follower or Personality."
Matsu_Yamamura = Personality(
    card_id=12463,
    title="Matsu Yamamura",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai, ScionOfTheWind],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
