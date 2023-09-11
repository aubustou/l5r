from __future__ import annotations

from l5r_auto.clans import (
    BrotherhoodOfShinsei,
    NinjaFaction,
    ShadowlandsFaction,
    SpiderClan,
)
from l5r_auto.keywords import (
    BogHag,
    Commander,
    Daimyo,
    DragonChild,
    Duelist,
    Expendable,
    Experienced,
    Goblin,
    Infiltrator,
    Monk,
    Ninja,
    Nonhuman,
    Reserve,
    Samurai,
    Shadowlands,
    Shugenja,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"After Atsushi enters play, lose 2 Honor. After Atsushi wins a duel, give him a +1F Infamy token.<br><b>Battle:</b> Fear 3 with +1 strength for each of Atsushi's Infamy tokens."
Daigotsu_Atsushi_Experienced = Personality(
    card_id=12161,
    title="Daigotsu Atsushi",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=10,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Unique, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists. You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i><br>After Hachiko enters play, lose 1 Honor."
Daigotsu_Hachiko = Personality(
    card_id=12162,
    title="Daigotsu Hachiko",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Reserve, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Give a target enemy Personality a Force penalty equal to his own Personal Honor. If his Force is now zero, you may give him a -1F/-1C <b>Poison </b>token and lose 1 Honor."
Daigotsu_Hayigi = Personality(
    card_id=12163,
    title="Daigotsu Hayigi",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[BogHag, Infiltrator, Nonhuman, Shadowlands, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> Shaoru challenges a target enemy Personality. Each player must focus at least once in the duel. Give the winner +1F."
Daigotsu_Shaoru = Personality(
    card_id=12164,
    title="Daigotsu Shaoru",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Kumoru's Followers must be Ninja.<br><b>Ninja Open:</b> Create a battlefield <i>(not at any Province)</i>. Assign Kumoru to attack there and another player's target unbowed Personality to defend there. Fight a battle there. Battle resolution there will not destroy Personalities. Lose 2 Honor."
Goju_Kumoru = Personality(
    card_id=12165,
    title="Goju Kumoru",
    force=3,
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
"<i>(You may Recruit a Reserve Personality, if they would be opposed, as an Absent Battle action.)</i><br>Mitsuru has +2F while opposing a Personality with no abilities."
Goju_Mitsuru = Personality(
    card_id=12166,
    title="Goju Mitsuru",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Reserve, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Ninja Battle:</b> Bow a target unbowed enemy Personality. If he has 0 Force or no abilities, create a 2F/2C/0PH <b>Ninja &#149; Shadowlands</b> Spider Clan Personality. Lose 1 Honor."
Goju_Yurishi_Experienced_2 = Personality(
    card_id=12167,
    title="Goju Yurishi",
    force=4,
    chi=4,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Experienced("2"), Unique, Daimyo, DragonChild, Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>After Gunjao enters play, lose 2 Honor.<br><b>Battle:</b> Fear 4 <i>(Bow a target enemy Follower or Personality without Followers with 4 or lower Force)</i>."
Kokujin_Gunjao = Personality(
    card_id=12168,
    title="Kokujin Gunjao",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, BrotherhoodOfShinsei, ShadowlandsFaction],
    keywords=[Duelist, Monk, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br>After Naibu enters play, lose 1 Honor."
Naibu = Personality(
    card_id=12169,
    title="Naibu",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[SpiderClan, ShadowlandsFaction],
    keywords=[Expendable, Commander, Goblin, Nonhuman, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After The Twisted One enters play, lose 1 Honor. <br><b>Ninja Battle:</b> Copy a Battle ability that does not copy abilities on a target enemy Personality. Remove the ability from the target."
The_Twisted_One = Personality(
    card_id=12170,
    title="The Twisted One",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[SpiderClan, NinjaFaction, ShadowlandsFaction],
    keywords=[Ninja, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
