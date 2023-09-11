from __future__ import annotations

from l5r_auto.clans import LionClan, SpiritFaction
from l5r_auto.keywords import (
    Ancestor,
    Cavalry,
    ChildOfProphecy,
    Commander,
    Destined,
    Duelist,
    Experienced,
    Hero,
    LoveLetter,
    Magistrate,
    Naval,
    Paragon,
    Samurai,
    Scout,
    Shugenja,
    Spirit,
    Tactician,
    TheMaskedLion,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Battle:</b> Straighten a target enemy unit in the Defender's home. Its controller may choose to move it to this battlefield. If he does not choose this, give this Province -2 strength."
Akodo_Raikitsu = Personality(
    card_id=11902,
    title="Akodo Raikitsu",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Duelist, Tactician, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card.)</i><br>Yuyama has +1F if you are Phoenix Clan."
Akodo_Yuyama = Personality(
    card_id=11905,
    title="Akodo Yuyama",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=6,
    clan=[LionClan, SpiritFaction],
    keywords=[Destined, Ancestor, Samurai, Scout, Spirit, TheMaskedLion],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Open:</b> Give Ayumi's target Follower <b>Cavalry</b>."
Ikoma_Ayumi_Experienced = Personality(
    card_id=11903,
    title="Ikoma Ayumi",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Cavalry, Naval, Experienced("1"), Hero, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Open, :g3::</b> If Suzaki is in your Province and you are Lion Clan, you may shuffle her into your deck to gain 1 Honor and create a 2F/2C/3PH <b>Lion Clan &#149; Ancestor &#149; Samurai &#149; Spirit</b> Personality in your home."
Kitsu_Suzaki = Personality(
    card_id=11904,
    title="Kitsu Suzaki",
    force=0,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[ChildOfProphecy, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Hachiro has +2F while attacking.<br><b>Unstoppable Battle:</b> Melee 2 Attack, or Melee 3 Attack if the target is Scorpion Clan. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Matsu_Hachiro_Experienced = Personality(
    card_id=11906,
    title="Matsu Hachiro",
    force=2,
    chi=3,
    personal_honor=4,
    gold_cost=9,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Cavalry, Commander, Experienced("1"), Paragon, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle:</b> If Misato is opposed, target a player. He discards a card at random to draw a card. Give Misato +1F."
Matsu_Misato_the_Hatamoto = Personality(
    card_id=11907,
    title="Matsu Misato, the Hatamoto",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[LoveLetter, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
