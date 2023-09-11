from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan, NagaFaction
from l5r_auto.keywords import (
    Alchemist,
    ClanChampion,
    Duelist,
    Earth,
    Experienced,
    Imperial,
    Kensai,
    Loyal,
    Monk,
    Naga,
    Samurai,
    Shugenja,
    SoulOf,
    Tattooed,
    TheLaughingDragon,
    Unique,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i><i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i></i>"
Mirumoto_Higaru = Personality(
    card_id=11166,
    title="Mirumoto Higaru",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=3,
    clan=[DragonClan],
    keywords=[Kensai, Samurai, SoulOf("Mirumoto Rosanjin")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> Fear 2, or Fear 3 if the target is dishonorable."
Mirumoto_Hikuryo = Personality(
    card_id=11167,
    title="Mirumoto Hikuryo",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[DragonClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br><b>Battle:</b> Niwa challenges a target enemy Personality. He may refuse; if he does, give Niwa +3F. Give the duel's loser -3F."
Mirumoto_Niwa = Personality(
    card_id=11168,
    title="Mirumoto Niwa",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Kensai, Samurai, SoulOf("Mirumoto Kei")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Nokkai has +1F/+1C while dueling, or opposed by, a Phoenix Clan Personality.<br>After the first time each turn Nokkai challenges a Personality, draw a card."
Mirumoto_Nokkai = Personality(
    card_id=11169,
    title="Mirumoto Nokkai",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[DragonClan],
    keywords=[Samurai, SoulOf("Mirumoto Tsuge"), Tattooed],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Limited:</b> Look at the top three cards of your Fate deck. You may exchange one of them with one from your hand. Put the cards back in any order.<br><b>Battle/Open:</b> Straighten your target Ring."
Mirumoto_Shikei_the_Laughing_Dragon_Experienced = Personality(
    card_id=11170,
    title="Mirumoto Shikei, the Laughing Dragon",
    force=4,
    chi=5,
    personal_honor=4,
    gold_cost=10,
    honor_requirement=9,
    clan=[DragonClan, BrotherhoodOfShinsei, NagaFaction],
    keywords=[
        Duelist,
        Kensai,
        Loyal,
        Unique,
        ClanChampion,
        Experienced("1"),
        Monk,
        Naga,
        Samurai,
        Tattooed,
        TheLaughingDragon,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br><b>Battle:</b> Bow a target enemy Personality with lower Force and lower Chi."
Mirumoto_Tsukazu = Personality(
    card_id=11171,
    title="Mirumoto Tsukazu",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=3,
    clan=[DragonClan],
    keywords=[Kensai, Samurai, SoulOf("Mirumoto Minawa")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> After you Recruit Yasushi, give him a +1F or +1C token."
Mirumoto_Yasushi = Personality(
    card_id=11172,
    title="Mirumoto Yasushi",
    force=4,
    chi=4,
    personal_honor=2,
    gold_cost=9,
    honor_requirement=4,
    clan=[DragonClan],
    keywords=[Samurai, SoulOf("Mirumoto Kyuzo")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Shugenja may attach and cast Spells.)</i><br><b>Earth Battle:</b> Discard a Kiho or a Spell from your hand to give this Province a strength bonus equal to the card's Focus Value."
Tamori_Katsumi = Personality(
    card_id=11173,
    title="Tamori Katsumi",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[DragonClan],
    keywords=[Earth, Shugenja, SoulOf("Tamori Shaitung")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Earth Limited, :bow::</b> Shaisen prays to the Fortunes. If you control a Temple, gain 1 Honor. You may bow your Temple to straighten Shaisen."
Tamori_Shaisen = Personality(
    card_id=11175,
    title="Tamori Shaisen",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=0,
    clan=[DragonClan],
    keywords=[Alchemist, Earth, Imperial, Shugenja, SoulOf("Tamori Shosei")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Ango has +1F/+1C for each Ring you control."
Togashi_Ango = Personality(
    card_id=11176,
    title="Togashi Ango",
    force=1,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=0,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, SoulOf("Togashi Chikato"), Tattooed],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Discard a Kiho to give Ogure +2F, or +3F if he is defending. <br><b>Battle:</b> Bow your target unbowed Ring. Take two additional Battle actions."
Togashi_Ogure = Personality(
    card_id=11177,
    title="Togashi Ogure",
    force=3,
    chi=4,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[DragonClan, BrotherhoodOfShinsei],
    keywords=[Monk, SoulOf("Hoshi Akiyama")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
