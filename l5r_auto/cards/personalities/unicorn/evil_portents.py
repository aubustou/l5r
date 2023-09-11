from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    BattleMaiden,
    Cavalry,
    Commander,
    DeathPriest,
    Destined,
    Experienced,
    Magistrate,
    Naval,
    Resilient,
    Samurai,
    Shugenja,
    Water,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"Your Honor cards out of play have <b>Courage</b>. <br><b>Battle:</b> Target an enemy card. If it has more Force, is Nonhuman, is Phoenix Clan, or has no attachments, bow it."
Moto_Chinua_Experienced = Personality(
    card_id=12493,
    title="Moto Chinua",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Cavalry, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i><br><b>Battle, :bow::</b> Fear equal to Dai-ketsu's Force plus the number of Spells he has. If there is a dead Personality in any discard pile or you are Mantis Clan, straighten Dai-ketsu."
Moto_Daiketsu = Personality(
    card_id=12494,
    title="Moto Dai-ketsu",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, Naval, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Jengzan's Cavalry Followers have <b>Resilient</b>. Your Cavalry Followers out of play have <b>Honor</b>. <i>(Repeatable Interrupt: Discard an Honor card to give an Honor gain or loss +1 or -1.)</i>"
Moto_Jengzan = Personality(
    card_id=12495,
    title="Moto Jengzan",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Resilient, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Home Interrupt:</b> After a Personality is rehonored for the action's effects <i>(including Honor gain)</i>, gain 1 Honor.<br><b>Battle:</b> Give a target enemy Personality -2F. Dishonor the target if he or she has lower Personal Honor than Dogenda."
Shinjo_Dogenda = Personality(
    card_id=12496,
    title="Shinjo Dogenda",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle. Draw a card after you Recruit a Destined card.)</i>"
Shinjo_Megura = Personality(
    card_id=12497,
    title="Shinjo Megura",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[UnicornClan],
    keywords=[Cavalry, Destined, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Tireless Battle:</b> Straighten Yabusame if she is attacking and your Family Honor is higher than any other player's.<br><b>Repeatable Battle, :bow::</b> Ranged 3 Attack. Gain 1 Honor."
Utaku_Yabusame = Personality(
    card_id=12498,
    title="Utaku Yabusame",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=8,
    honor_requirement=6,
    clan=[UnicornClan],
    keywords=[Cavalry, BattleMaiden, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
