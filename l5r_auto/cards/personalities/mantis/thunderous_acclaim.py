from __future__ import annotations

from l5r_auto.clans import MantisClan, NagaFaction
from l5r_auto.keywords import (
    Artisan,
    Destined,
    Earth,
    Kensai,
    Magistrate,
    Naga,
    Naval,
    Prophetess,
    Reserve,
    Resilient,
    Samurai,
    Shugenja,
    Thunder,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"After a card enters another player's hand from his or her own card's effect, target your Personality with fewer Omen tokens than his Personal Honor, and give him a +1F/+1C Omen token."
Kitsune_Narako = Personality(
    card_id=12308,
    title="Kitsune Narako",
    force=0,
    chi=2,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Destined, Earth, Prophetess, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 2 Attack. Straighten Kyan if you have <b>Compassion </b>or the target was Dragon Clan. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Moshi_Kyan = Personality(
    card_id=12309,
    title="Moshi Kyan",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Resilient, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Positive numerals in the text box of Akira's Bow Items have +1. <i>(2 is a numeral, two is not.)</i><br><b>Battle, :bow::</b> Ranged 4 Attack. If this is not increased or combined, it can target a Province and reduce its strength by the Ranged Attack's strength."
Tsuruchi_Akira = Personality(
    card_id=12310,
    title="Tsuruchi Akira",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: Kinshikirai's printed ability has no Gold Cost. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i><br><b>Interrupt, :g2::</b> If the action is yours or you are Lion Clan, after it resolves, straighten Kinshikirai."
Yoritomo_Kinshikirai = Personality(
    card_id=12311,
    title="Yoritomo Kinshikirai",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Magistrate, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i> <br>After Kyunan enters play, you may take one or two additional actions to Equip Peasant Weapons to him."
Yoritomo_Kyunan = Personality(
    card_id=12312,
    title="Yoritomo Kyunan",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Kensai, Reserve, Artisan, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Minoko has Naval while she has a Peasant Weapon.<br><b>Battle, :bow::</b> Melee 3 Attack. If this does not destroy a Personality, straighten Minoko."
Yoritomo_Minoko = Personality(
    card_id=12313,
    title="Yoritomo Minoko",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=None,
    clan=[MantisClan, NagaFaction],
    keywords=[Kensai, Naga, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
