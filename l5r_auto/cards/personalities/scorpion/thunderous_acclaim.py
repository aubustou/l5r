from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    Air,
    BitterLies,
    Courtier,
    Duelist,
    Experienced,
    Kensai,
    Ninja,
    Resilient,
    Samurai,
    Shugenja,
    Tactician,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Once per game per card, a Resilient card does not die in battle resolution. Battle: Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i><br><b> Battle:</b> Give a target enemy Personality -2F. Bow him if he is Lion Clan."
Bayushi_Chizuken = Personality(
    card_id=12320,
    title="Bayushi Chizuken",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Resilient, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"You Recruit Doji Natsuyo for 1 less Gold.<br><b>Political Open:</b> Target two Personalities controlled by the same player. <i>Fuyuko sows seeds of distrust.</i> After the next time this turn they are attacking in the same army together, their controller loses 1 Honor, or 2 Honor if each of them has 3 or more printed Personal Honor."
Bayushi_Fuyuko_Experienced = Personality(
    card_id=12321,
    title="Bayushi Fuyuko",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open:</b> Remove a Madness token from Tenburo to give him <b>Cavalry, Conqueror, </b>or<b> Naval</b>."
Bayushi_Tenburo = Personality(
    card_id=12322,
    title="Bayushi Tenburo",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Kanako enters play, lose 2 Honor.<br>Compassion, or if you are Crab Clan: Kanako has Destined. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Shosuro_Kanako = Personality(
    card_id=12323,
    title="Shosuro Kanako",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Resilient, Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons.)</i><br>After Wayari enters play, give a target Personality a Madness token."
Shosuro_Wayari = Personality(
    card_id=12324,
    title="Shosuro Wayari",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Mumoshi enters play, lose 2 Honor.<br><b>Ninja Battle, :bow::</b> Ranged 2 Attack. Straighten Mumoshi if he has a Ninja Weapon or the target has a Poison token."
Soshi_Mumoshi = Personality(
    card_id=12325,
    title="Soshi Mumoshi",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Air, Ninja, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
