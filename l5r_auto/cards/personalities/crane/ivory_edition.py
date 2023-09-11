from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Air,
    Artisan,
    ClanChampion,
    Courtier,
    Duelist,
    Experienced,
    Governor,
    Loyal,
    Magistrate,
    Samurai,
    Scout,
    Seductress,
    Shugenja,
    SoulOf,
    TheSmilingBlade,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i><i>(Shugenja may attach and cast Spells.)</i></i>"
Asahina_Umeko = Personality(
    card_id=11155,
    title="Asahina Umeko",
    force=0,
    chi=4,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[CraneClan],
    keywords=[Air, Shugenja, SoulOf("Asahina Kimita")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 4 Attack <i>(Destroy a target enemy Follower, or Personality without Followers, with 4 or lower Force)</i>."
Daidoji_Kinta = Personality(
    card_id=11156,
    title="Daidoji Kinta",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Samurai, SoulOf("Daidoji Gudeta")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
Daidoji_Tanshi = Personality(
    card_id=11157,
    title="Daidoji Tanshi",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Engage:</b> Raise Ujirou's Force, and the Force of a target Personality in his army, to equal the Force of a target enemy card."
Daidoji_Ujirou = Personality(
    card_id=11158,
    title="Daidoji Ujirou",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=3,
    clan=[CraneClan],
    keywords=[Samurai, Scout, SoulOf("Daidoji Gempachi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Bow a target enemy dishonorable Personality. Raise or lower this Province's strength by Etsuki's Personal Honor."
Doji_Etsuki = Personality(
    card_id=11159,
    title="Doji Etsuki",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Governor, Magistrate, Samurai, SoulOf("Doji Numata")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Katata cannot attack or defend. You may take Favor Battle actions one additional time per turn. <br><b>Political Home Battle/Open, :bow::</b> Take the Imperial Favor."
Doji_Katata = Personality(
    card_id=11160,
    title="Doji Katata",
    force=0,
    chi=1,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=8,
    clan=[CraneClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Your other Crane Clan Personalities have +1PH.<br><b>Favor Political Limited:</b> Discard the Imperial Favor to draw a card."
Doji_Makoto_the_Smiling_Blade_Experienced = Personality(
    card_id=11161,
    title="Doji Makoto, the Smiling Blade",
    force=3,
    chi=6,
    personal_honor=5,
    gold_cost=10,
    honor_requirement=10,
    clan=[CraneClan],
    keywords=[
        Duelist,
        Loyal,
        Unique,
        ClanChampion,
        Courtier,
        Experienced("1"),
        Samurai,
        TheSmilingBlade,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Limited:</b> Discard the top card of your Fate deck. Target another player, who may choose to lose 2 Honor. If he does not choose this, gain Honor equal to the card's Focus Value."
Doji_Shirarou = Personality(
    card_id=11162,
    title="Doji Shirarou",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Artisan, Samurai, SoulOf("Doji Bukita")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open:</b> Target a Personality with lower Personal Honor than Soeka's Chi. Set his Force equal to his own Chi."
Doji_Soeka = Personality(
    card_id=11163,
    title="Doji Soeka",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, Magistrate, Seductress, SoulOf("Doji Nenkai")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Political Limited, :bow::</b> Another player's target Personality may challenge Amiki. If he does not, his abilities may not be used until your next turn begins. Destroy the duel's loser."
Kakita_Amiki = Personality(
    card_id=11164,
    title="Kakita Amiki",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Courtier, Samurai, SoulOf("Kakita Funaki")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> Fear 1, with +1 strength if Ibara has challenged a Personality this turn."
Kakita_Ibara = Personality(
    card_id=11165,
    title="Kakita Ibara",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[CraneClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
