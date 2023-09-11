from __future__ import annotations

from l5r_auto.clans import CrabClan
from l5r_auto.keywords import (
    Commander,
    Daimyo,
    Earth,
    Experienced,
    Jade,
    Loyal,
    Magistrate,
    Reserve,
    Resilient,
    Samurai,
    Shugenja,
    Siege,
    Tactician,
    Unique,
    WitchHunter,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Battle:</b> Melee 1 Attack, with +2 strength if Genda has a Heavy Weapon or has used his rulebook Tactical Advantage ability this turn."
Hida_Genda = Personality(
    card_id=12440,
    title="Hida Genda",
    force=4,
    chi=2,
    personal_honor=1,
    gold_cost=9,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Tactician, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Other players' Melee and Ranged attacks targeting cards in Eichi's unit have a strength penalty equal to the number of your Fortifications at his battlefield.<br><b>Battle:</b> Take an additional action from your Fortification, even if it is at an adjacent battlefield."
Kaiu_Eichi = Personality(
    card_id=12441,
    title="Kaiu Eichi",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=3,
    clan=[CrabClan],
    keywords=[Resilient, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"O-Taro enters play for 1 less Gold during battle for each Fortification attached to the current Province. After you discard a card for an Honor action, give O-Taro +1F. You may Proclaim O-Taro even if it is not your turn."
Kaiu_OTaro = Personality(
    card_id=12442,
    title="Kaiu O-Taro",
    force=4,
    chi=2,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[CrabClan],
    keywords=[Reserve, Samurai, Siege],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Hokinsha has +1C if you are Mantis Clan or have <b>Courtesy</b>. <i>(Courtesy does not take effect if you went first.)</i><br><b>Battle:</b> Straighten your Sensei. You may use its abilities a second time this turn. Take an additional action."
Kuni_Hokinsha = Personality(
    card_id=12443,
    title="Kuni Hokinsha",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Your Provinces have +1 strength. Your Earth Personalities <i>(including Renyu)</i> have <b>Resilient</b>.<br><b>Earth Jade Tireless Battle:</b> Straighten your target Earth Personality. You may target and bow an enemy card with Shadowlands or with lower Force than Renyu."
Kuni_Renyu_Experienced_4 = Personality(
    card_id=12444,
    title="Kuni Renyu",
    force=5,
    chi=5,
    personal_honor=2,
    gold_cost=12,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[
        Experienced("4"),
        Loyal,
        Unique,
        Daimyo,
        Earth,
        Jade,
        Magistrate,
        Shugenja,
        WitchHunter,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Tenba has Cavalry while you are the Defender and he has an Earth Spell.<br><b>Battle:</b> Give a target enemy Follower or Personality -3F."
Kuni_Tenba = Personality(
    card_id=12445,
    title="Kuni Tenba",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[CrabClan],
    keywords=[Earth, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
