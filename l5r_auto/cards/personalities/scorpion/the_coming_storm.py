from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    BitterLies,
    Courtier,
    Expendable,
    Junshin,
    Kensai,
    Mastermind,
    Ninja,
    SakeAddict,
    Samurai,
    Spy,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Kensai may attach two Weapons, as long as neither is Two-Handed.)</i> <br><b>Battle:</b> Give a target enemy Personality a Force penalty equal to Akagi's Force."
Bayushi_Akagi = Personality(
    card_id=11764,
    title="Bayushi Akagi",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After another player's Personality Lobbies, give him -1PH, or -2PH if he is Crane Clan.<br><b>Political Open, :bow::</b> Target a Personality whose current Personal Honor is lower than printed. His controller loses 1 Honor."
Bayushi_Fuyuko = Personality(
    card_id=11765,
    title="Bayushi Fuyuko",
    force=1,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> After you Recruit Jinn-Ja, put a target non-Unique Political Strategy in your discard pile into your hand."
Bayushi_JinnJa = Personality(
    card_id=11766,
    title="Bayushi Jinn-Ja",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Mastermind, SakeAddict],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br>Invest :g2:: Dishonor one or two target Personalities with lower Personal Honor. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i>"
Bayushi_Kotomuri = Personality(
    card_id=11767,
    title="Bayushi Kotomuri",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Expendable, Junshin, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Melee 2 Attack, or Melee 3 Attack if the target is dishonorable <i>(Destroy a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Melee Attack's strength)</i>."
Shosuro_Kayo = Personality(
    card_id=11768,
    title="Shosuro Kayo",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Ninja Battle:</b> Give a target enemy Personality a -1F/-1C <b>Poison </b>token. You may move Sadao home if the target was Lion Clan."
Shosuro_Sadao = Personality(
    card_id=11769,
    title="Shosuro Sadao",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Ninja, Samurai, Spy],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
