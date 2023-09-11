from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Destined,
    Earth,
    Experienced,
    Jade,
    Resilient,
    Samurai,
    Shugenja,
    Siege,
    TheMaskedTortoise,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i> <br><b>Jade Battle, :bow::</b> Melee 3 Attack. Straighten Toranosuke if he has a Heavy Weapon or if the target is Shadowlands."
Hida_Toranosuke_Experienced = Personality(
    card_id=12284,
    title="Hida Toranosuke",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Resilient, Experienced("1"), Jade, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card.)</i><br>Compassion: Gizen has +1F for each Fortification at his battlefield, to a maximum of 3 Fortifications. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Kaiu_Gizen = Personality(
    card_id=12285,
    title="Kaiu Gizen",
    force=0,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=2,
    clan=[CrabClan],
    keywords=[Destined, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'<b>Invest :g1::</b> Create a Fortification Holding with the trait "This Province has +1 strength" and attach it to your target Province.<br><b>Open:</b> If it is not your turn, target your Fortification. Before this turn ends, if it is still in play, gain 1 Honor.'
Kaiu_Otogou = Personality(
    card_id=12286,
    title="Kaiu Otogou",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Invest :g5:, or :g3: if any other player is Crane Clan: Give Igarasu two +1F/+1C tokens."
Kuni_Igarasu = Personality(
    card_id=12287,
    title="Kuni Igarasu",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=3,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Earth Battle:</b> Melee 3 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 3 or lower Force)</i>."
Kuni_Soseki = Personality(
    card_id=12288,
    title="Kuni Soseki",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=10,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Resilient, Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Fear 4. Straighten Suppon if you are Scorpion Clan or if your army has fewer units than the enemy army."
Toritaka_Suppon = Personality(
    card_id=12289,
    title="Toritaka Suppon",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=2,
    clan=[CrabClan],
    keywords=[Samurai, TheMaskedTortoise],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
