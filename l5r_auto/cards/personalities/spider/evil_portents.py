from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ShadowlandsFaction, SpiderClan
from l5r_auto.keywords import (
    Conqueror,
    Destined,
    Duelist,
    Experienced,
    Infiltrator,
    Ninja,
    Nonhuman,
    Ogre,
    Resilient,
    Samurai,
    Shadowlands,
    Undead,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> Give a target enemy Follower or Personality -3F. If it now has lower Force than Aimaro, give Aimaro +1C <i>(this turn)</i>."
Daigotsu_Aimaro = Personality(
    card_id=12482,
    title="Daigotsu Aimaro",
    force=2,
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
"You may Recruit Endo from the discard pile even if he is dead. Endo is not destroyed for having 0 Chi. Your Honor cards out of play have <b>Courage</b>.<br><b>Battle:</b> Fear 2, or Fear 4 if the target is Shadowlands."
Daigotsu_Endo_Experienced = Personality(
    card_id=12483,
    title="Daigotsu Endo",
    force=4,
    chi=0,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Destined, Experienced("1"), Nonhuman, Samurai, Shadowlands, Undead],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Yuhmi enters play, lose 4 Honor.<br><b>Battle:</b> Fear 4 that destroys Shugenja after it bows them."
Daigotsu_Yuhmi_Experienced_2 = Personality(
    card_id=12484,
    title="Daigotsu Yuhmi",
    force=6,
    chi=2,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Experienced("2"), Unique, Infiltrator, Nonhuman, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Iaitsu enters play, lose 2 Honor. <br><b>Ninja Battle, :bow::</b> Ranged 3 Attack. Straighten Iaitsu if this destroyed a card without abilities <i>(Destroy a target enemy Follower or Personality without Followers with 3 or lower Force)</i>."
Goju_Iaitsu = Personality(
    card_id=12485,
    title="Goju Iaitsu",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle.)</i><br>After Toriken enters play, lose 1 Honor. <br><b>Ninja Open:</b> Remove an ability from a target non-Unique Follower or Personality."
Goju_Toriken = Personality(
    card_id=12486,
    title="Goju Toriken",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Conqueror, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Hikayo's Weapons must be Heavy Weapons. Shadowlands Personalities may not refuse challenges from Hikayo.<br><b>Interrupt:</b> Hikayo's duel stat in duels from the action is his printed Force."
Hikayo = Personality(
    card_id=12487,
    title="Hikayo",
    force=5,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Resilient, Nonhuman, Ogre, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
