from __future__ import annotations

from l5r_auto.clans import CraneClan
from l5r_auto.keywords import (
    Artisan,
    Courtier,
    Duelist,
    Expendable,
    Experienced,
    Jester,
    Kensai,
    Magistrate,
    Resilient,
    Samurai,
    TheMaskedCrane,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"After the first time each turn you resolve an Honor action, give Ikei a +1F Respect token if he has two or fewer Respect tokens."
Doji_Ikei = Personality(
    card_id=12446,
    title="Doji Ikei",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Resilient, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Ignore Natsuyo's Honor Requirement while you control Bayushi Fuyuko. <br><b>Political Home Interrupt, :bow::</b> When taking Honor Interrupts to the action, you may remove Political Honor cards in your discard pile from the game instead of discarding them from your hand."
Doji_Natsuyo_Experienced = Personality(
    card_id=12447,
    title="Doji Natsuyo",
    force=1,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=8,
    clan=[CraneClan],
    keywords=[Courtier, Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Open:</b> Remove an ability from a target Holding or attachment.<br><b>Tireless Battle:</b> Move Soeka home. <i>(Tireless actions may be taken even while bowed.)</i>"
Doji_Soeka_Experienced = Personality(
    card_id=12448,
    title="Doji Soeka",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[CraneClan],
    keywords=[Courtier, Experienced("1"), Magistrate],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Cards focused by Daitsu's opponent in duels have -1FV while you control, or the opponent is, Kakita Shinichi. Daitsu will only attach one Weapon.<br><b>Iaijutsu Battle, :bow::</b> Melee 3 Attack. You may bow a Sword attached to Daitsu to straighten him."
Kakita_Daitsu_Experienced = Personality(
    card_id=12449,
    title="Kakita Daitsu",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=5,
    clan=[CraneClan],
    keywords=[Duelist, Kensai, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Battle, :bow::</b> Move home a target enemy dishonorable Personality."
Kakita_Inaka = Personality(
    card_id=12450,
    title="Kakita Inaka",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CraneClan],
    keywords=[Artisan, Courtier, Jester],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Melee and Ranged Attacks targeting Oshaberi have -3 strength.<br><b>Political Engage:</b> Other players do not gain Honor for destroying your cards in this battle's resolution.<br><b>Political Open, :bow::</b> Straighten your Sensei."
Kakita_Oshaberi = Personality(
    card_id=12451,
    title="Kakita Oshaberi",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=4,
    clan=[CraneClan],
    keywords=[Expendable, Artisan, Courtier, TheMaskedCrane],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
