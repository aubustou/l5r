from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Braggart,
    Courtier,
    Destined,
    Duelist,
    Imperial,
    Jester,
    Magistrate,
    Reserve,
    Samurai,
    Scout,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action.)</i><br><b>Absent Interrupt:</b> After you Recruit Ryushi, give him +2F."
Daidoji_Ryushi = Personality(
    card_id=11734,
    title="Daidoji Ryushi",
    force=2,
    chi=1,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=2,
    clan=[CraneClan],
    keywords=[Reserve, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Give a target Personality that has moved or entered play this battle +2F or -2F."
Daidoji_Sutebo = Personality(
    card_id=11735,
    title="Daidoji Sutebo",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Natsuyo enters play for 1 less Gold if another player is Scorpion Clan.<br><b>Favor Political Open, :bow::</b> Discard the Imperial Favor to gain 1 Honor."
Doji_Natsuyo = Personality(
    card_id=11736,
    title="Doji Natsuyo",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> If the action creates a duel involving Burei, ignore Items' Chi Modifiers in the duel's resolution.<br><b>Iaijutsu Battle:</b> Give a target enemy Personality -3F."
Kakita_Burei = Personality(
    card_id=11737,
    title="Kakita Burei",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Artisan, Braggart, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Political Open, :bow::</b> Target a Personality. After the next time he assigns to attack a Province with a Fortification, target a player who gains or loses 1 Honor."
Kakita_Jikeru = Personality(
    card_id=11738,
    title="Kakita Jikeru",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card. Duelists win tied duels versus non-Duelists.)</i>"
Kakita_Mitohime = Personality(
    card_id=11739,
    title="Kakita Mitohime",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Destined, Duelist, Imperial, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
