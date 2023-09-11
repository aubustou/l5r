from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    ClanChampion,
    Courtier,
    Destined,
    Experienced,
    Loyal,
    Magistrate,
    Ninja,
    Samurai,
    ShojusSoul,
    Sociopath,
    SoulOf,
    Spy,
    ThePoisonMask,
    Unique,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Political Home Battle, :bow::</b> Target a Personality. His controller may dishonor him. If he did not become dishonorable <i>(or was already dishonorable)</i>, give him -3F."
Bayushi_Akane = Personality(
    card_id=11210,
    title="Bayushi Akane",
    force=0,
    chi=3,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Courtier, SoulOf("Bayushi Kurumi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After another player's Battle action targets a Courtier at Dakatsu's location, the player loses 2 Honor."
Bayushi_Dakatsu = Personality(
    card_id=11211,
    title="Bayushi Dakatsu",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=1,
    clan=[ScorpionClan],
    keywords=[Magistrate, Samurai, SoulOf("Shosuro Takagi"), Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> Fear 2. This may target a Personality with Followers if he has 0 Personal Honor <i>(Bow a target enemy Follower, or Personality without Followers, with 2 or lower Force)</i>."
Bayushi_Masashi = Personality(
    card_id=11212,
    title="Bayushi Masashi",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Ranged Attacks targeting Meiko have -3 strength.<br><b>Battle:</b> Give a target enemy Personality -3F. Dishonor him if his Force is now 0."
Bayushi_Meiko = Personality(
    card_id=11213,
    title="Bayushi Meiko",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai, SoulOf("Bayushi Maemi")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"You may use your Stronghold's abilities twice per turn.<br><b>Political Limited/Engage:</b> Dishonor a target Personality."
Bayushi_Nitoshi_the_Poison_Mask_Experienced_2 = Personality(
    card_id=11214,
    title="Bayushi Nitoshi, the Poison Mask",
    force=5,
    chi=5,
    personal_honor=1,
    gold_cost=12,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[
        Experienced("2"),
        Loyal,
        Unique,
        ClanChampion,
        Courtier,
        Ninja,
        Samurai,
        ShojusSoul,
        Sociopath,
        ThePoisonMask,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Political Open:</b> Target a Personality. After the next time <i>(this turn)</i> his controller assigns him, targets him, or resolves an action on a card in his unit, his controller loses Honor equal to his Personal Honor, then dishonor him."
Bayushi_Shizuka = Personality(
    card_id=11215,
    title="Bayushi Shizuka",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai, SoulOf("Bayushi Saya")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Invest :g2::</b> Discard a card from your hand to make a target player lose Honor equal to half the Focus Value, rounded up."
Shosuro_Hotaka = Personality(
    card_id=11216,
    title="Shosuro Hotaka",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Destined, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Ninja Battle, :bow::</b> Ranged 3 Attack. You may discard a card to straighten Keiichi."
Shosuro_Keiichi = Personality(
    card_id=11217,
    title="Shosuro Keiichi",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Ninja, Samurai, SoulOf("Shosuro Osamito")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Ninja Battle:</b> Discard a card from this Province. If the card is a Personality, give Tagiso +2F."
Shosuro_Tagiso = Personality(
    card_id=11218,
    title="Shosuro Tagiso",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Ninja, Samurai, SoulOf("Shosuro Hihiko")],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Limited:</b> Choose a Province and turn its card face-up <i>(if necessary)</i>. Reduce the Province's strength by the Personal Honor of any Personality in it."
Shosuro_Tosaku = Personality(
    card_id=11219,
    title="Shosuro Tosaku",
    force=3,
    chi=4,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Samurai, SoulOf("Bayushi Tai"), Spy],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
