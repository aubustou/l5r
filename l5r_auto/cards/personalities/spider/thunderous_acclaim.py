from __future__ import annotations

from l5r_auto.clans import (
    BrotherhoodOfShinsei,
    NinjaFaction,
    ShadowlandsFaction,
    SpiderClan,
)
from l5r_auto.keywords import (
    Cavalry,
    ClanChampion,
    Conqueror,
    Duelist,
    Expendable,
    Experienced,
    Kensai,
    Loyal,
    Monk,
    Ninja,
    Paragon,
    Samurai,
    Shadowlands,
    Shugenja,
    Unique,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Maho Battle:</b> Fear equal to the Force of your target Personality; destroy him if he is bowed, and bow him if he is unbowed."
Chuda_Teraiko = Personality(
    card_id=12326,
    title="Chuda Teraiko",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Shadowlands, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'After Kanpeki enters play, lose 3 Honor.<br>Your Fear effects may target Items and Spells. Your Shadowlands Personalities without a printed Fear ability have the ability, "<b>Battle:</b> Fear 2."<br><b>Battle:</b> Fear 5.'
Daigotsu_Kanpeki_Unleashed_Experienced_4 = Personality(
    card_id=12327,
    title="Daigotsu Kanpeki, Unleashed",
    force=7,
    chi=5,
    personal_honor=0,
    gold_cost=15,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[
        Conqueror,
        Experienced("4"),
        Kensai,
        Loyal,
        Unique,
        ClanChampion,
        Monk,
        Paragon,
        Samurai,
        Shadowlands,
    ],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Onita has +1F/+1C while she has a Sword.<br><b>Open:</b> Give Onita +2F/-2C. Duels in which she is the challenger are duels of Force <i>(this turn)</i>."
Daigotsu_Onita = Personality(
    card_id=12328,
    title="Daigotsu Onita",
    force=1,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Duelist, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: If Spider Clan is your only Clan Alignment, you may Recruit Tomiyama as an Open. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Daigotsu_Tomiyama = Personality(
    card_id=12329,
    title="Daigotsu Tomiyama",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Duelist, Expendable, Samurai, Shadowlands, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Kenteiru enters play, lose 3 Honor.<br>Compassion: Kenteiru has Naval. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Goju_Kenteiru = Personality(
    card_id=12330,
    title="Goju Kenteiru",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Cavalry, Ninja, Shadowlands, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Bow a target enemy Personality with lower Chi. If he has no abilities, create a 2F/2C/0PH <b>Ninja &#149; Shadowlands</b> Personality."
Ninube_Aitso = Personality(
    card_id=12331,
    title="Ninube Aitso",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
