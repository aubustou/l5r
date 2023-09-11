from __future__ import annotations

from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Courtier,
    Duelist,
    Expendable,
    Imperial,
    Kensai,
    Monk,
    Reserve,
    Samurai,
    Shadowlands,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Duelists win tied duels versus non-Duelists. Draw a card after your Expendable card dies.)</i><br><b>Battle:</b> Fear 2."
Daigotsu_Atsushi = Personality(
    card_id=11770,
    title="Daigotsu Atsushi",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Expendable, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br><b>Open, :bow::</b> Look at the top five cards of your Fate deck. You may rearrange them. Draw a card. Destroy Teruo."
Daigotsu_Teruo = Personality(
    card_id=11771,
    title="Daigotsu Teruo",
    force=0,
    chi=1,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Expendable, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i><br>After a Fear effect from a card in Nao's unit, or from your action that targeted Nao, bows a Follower, destroy it."
Nao = Personality(
    card_id=11772,
    title="Nao",
    force=2,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Before one of Sora's Weapons is destroyed, draw a card.<br><b>Battle, :bow::</b> Melee 2 Attack. You may bow Sora's Weapon to straighten him."
Sora = Personality(
    card_id=11773,
    title="Sora",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei],
    keywords=[Kensai, Monk],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an <b>Absent Battle</b> action.)</i><br>Mizuki's Reserve may be used as <b>Absent Battle/Engage</b>.<br>Invest :g1:: Take the Imperial Favor."
Susumu_Mizuki = Personality(
    card_id=11774,
    title="Susumu Mizuki",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Reserve, Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After your Spider Clan Personality is destroyed, gain 1 Honor.<br><b>Home Political Battle, :bow::</b> Destroy your target Spider Clan Personality to destroy a target enemy card without attachments."
Susumu_Takuan = Personality(
    card_id=11775,
    title="Susumu Takuan",
    force=2,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[SpiderClan],
    keywords=[Courtier, Imperial],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
