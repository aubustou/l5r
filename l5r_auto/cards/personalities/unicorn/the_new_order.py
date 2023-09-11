from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Cavalry,
    Commander,
    Conqueror,
    Courtier,
    DeathPriest,
    Hatamoto,
    Magistrate,
    Merchant,
    Samurai,
    ScionOfTheVoid,
    Shugenja,
    Void,
    Water,
    Zealot,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Hideshi's Invest is :g0: if another player is Phoenix Clan.<br><b>Invest :g2::</b> Permanently give another player's target Holding the trait, \"After this Holding bows, each player gains 1 Honor.\""
Ide_Hideshi_Topaz_Champion = Personality(
    card_id=11938,
    title="Ide Hideshi, Topaz Champion",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Cavalry, Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Courtesy: Igo has <b>Destined</b>. <i>(Courtesy traits do not take effect if you went first. Draw a card after you Recruit a Destined card.)</i>"
Ide_Igo = Personality(
    card_id=11939,
    title="Ide Igo",
    force=1,
    chi=3,
    personal_honor=3,
    gold_cost=4,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(A Conqueror's unit doesn't bow after battle. Shugenja may attach and cast Spells.)</i>"
Moto_Chizura = Personality(
    card_id=11942,
    title="Moto Chizura",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Conqueror, DeathPriest, Hatamoto, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action resolves, if its Fear effects bowed any cards without attachments, destroy them."
Moto_Nergui = Personality(
    card_id=11940,
    title="Moto Nergui",
    force=2,
    chi=4,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, DeathPriest, ScionOfTheVoid, Shugenja, Void, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Tadasu has +1F while you control a Death Priest.<br><b>Unstoppable Battle:</b> Fear 3 that may target Spells. Destroy any Spells this bowed. <i>(Spells have 0 Force.)</i>"
Moto_Tadasu = Personality(
    card_id=11941,
    title="Moto Tadasu",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=8,
    honor_requirement=0,
    clan=[UnicornClan],
    keywords=[Cavalry, Commander, Samurai, Zealot],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Saeki has +1F while in an army with any Ronin.<br><b>Battle:</b> Give a target enemy Personality -2F. If he has lower Personal Honor, give Saeki +1F."
Shinjo_Saeki = Personality(
    card_id=11943,
    title="Shinjo Saeki",
    force=2,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=3,
    clan=[UnicornClan],
    keywords=[Cavalry, Magistrate, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
