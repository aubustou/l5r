from __future__ import annotations

from l5r_auto.clans import (
    BrotherhoodOfShinsei,
    RatlingFaction,
    ShadowlandsFaction,
    Unaligned,
)
from l5r_auto.keywords import (
    Courtier,
    Experienced,
    Goblin,
    Heir,
    Imperial,
    Ishiken,
    Kolat,
    LoveLetter,
    MasterCoin,
    Merchant,
    Monk,
    Nonhuman,
    Ogre,
    OneTribe,
    Ratling,
    Resilient,
    Ronin,
    Scavenger,
    Scout,
    Shadowlands,
    Shugenja,
    Sinner,
    Unique,
    Void,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

'<i>(Once per game per card, a Resilient card does not die in battle resolution. Shugenja may attach and cast Spells.)</i> <br>Will not gain the "Phoenix Clan" Clan Alignment.'
Banished = Personality(
    card_id=11932,
    title="Banished",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[Unaligned],
    keywords=[Resilient, Ishiken, Ronin, Shugenja, Void],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Br'nn has +1F while he has an attachment. Br'nn has +1F while an attachment is in another player's discard pile. Br'nn has +1F while another player controls an Ashalan card."
Brnn_Experienced = Personality(
    card_id=11933,
    title="Br'nn",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[Unaligned, RatlingFaction],
    keywords=[Experienced("1"), Nonhuman, OneTribe, Ratling, Scavenger, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Will not gain a Clan Alignment. After your turn begins, if you control six other Love Letter cards with different titles and six Affection tokens, you win the game.<br><b>Favor Political Open, :bow::</b> Discard the Imperial Favor to draw a card."
Iweko_Miaka_the_Princess = Personality(
    card_id=11934,
    title="Iweko Miaka, the Princess",
    force=0,
    chi=5,
    personal_honor=4,
    gold_cost=6,
    honor_requirement=12,
    clan=[Unaligned],
    keywords=[Unique, Heir, Imperial, LoveLetter],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After Keppo enters play, lose 3 Honor. <br><b>Interrupt, [*]:</b> If the action Recruits Keppo or is his printed Battle action, after it resolves, Equip a target attachment from another player's discard pile to him.<br><b>Battle:</b> Destroy a target enemy attachment with 4 Gold Cost or less."
Keppo_Experienced = Personality(
    card_id=11936,
    title="Keppo",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Experienced("1"), Goblin, Nonhuman, Scout, Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After Masajiro enters play, lose 2 Honor. <br><b>Home Battle:</b> If he would be opposed, move Masajiro to the current battlefield. After he moves, straighten his attachments if there is another Nonhuman or Unique Personality in his army."
Masajiro = Personality(
    card_id=11935,
    title="Masajiro",
    force=5,
    chi=2,
    personal_honor=0,
    gold_cost=9,
    honor_requirement=None,
    clan=[Unaligned, ShadowlandsFaction],
    keywords=[Nonhuman, Ogre, Shadowlands, Sinner, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Other players' actions targeting The Abbot cost 2 more Gold <i>(even actions without Gold costs)</i>. <br>Invest :g1:: Gain a Conspiracy Token. You may give a target card you do not control a Clout Token. <br><b>Kolat Political Open:</b> Straighten a target Holding."
The_Abbot_Experienced_3 = Personality(
    card_id=11937,
    title="The Abbot",
    force=2,
    chi=4,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[Unaligned, BrotherhoodOfShinsei],
    keywords=[
        Experienced("3 Yasuki Jinn-Kuen"),
        Unique,
        Courtier,
        Kolat,
        MasterCoin,
        Merchant,
        Monk,
    ],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
