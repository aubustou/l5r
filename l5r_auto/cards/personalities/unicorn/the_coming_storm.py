from __future__ import annotations

from l5r_auto.clans import UnicornClan
from l5r_auto.keywords import (
    Cavalry,
    Courtier,
    DeathPriest,
    Expendable,
    Merchant,
    Samurai,
    Shugenja,
    StableMaster,
    Water,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>:bow::</b> Produce Gold equal to Aragaki's Personal Honor, which may only pay for one Invest cost."
Ide_Aragaki = Personality(
    card_id=11781,
    title="Ide Aragaki",
    force=1,
    chi=2,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
'Invest :g2:: Create a <i>(bowed)</i> Holding with the trait, "<b>:bow::</b> Produce 1 Gold."<br><b>Economic Home Battle/Open, :g1::</b> Straighten your target Courtier, Unicorn Clan, or Spider Clan Personality.'
Ide_Kosaka = Personality(
    card_id=11782,
    title="Ide Kosaka",
    force=2,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[UnicornClan],
    keywords=[Courtier, Merchant],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Draw a card after your Expendable card dies.)</i><br><b>Tireless Battle:</b> Erdene commits Seppuku. Bow a target enemy card. <i>(Rehonor, then destroy, a Personality who commits Seppuku; these effects cannot be negated.)</i>"
Moto_Erdene = Personality(
    card_id=11783,
    title="Moto Erdene",
    force=2,
    chi=1,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Expendable, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an <b>Absent Engage</b>, move your unbowed Personality in a Cavalry unit to this battle. Shugenja may attach and cast Spells.)</i> <br>Qorin has <b>Naval</b> while he has a Water Spell."
Moto_Qorin = Personality(
    card_id=11784,
    title="Moto Qorin",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Cavalry, DeathPriest, Shugenja, Water],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Battle, :bow::</b> Ranged 2 Attack. If Ajasu has moved this battle, straighten him."
Shinjo_Ajasu_Topaz_Champion = Personality(
    card_id=11785,
    title="Shinjo Ajasu, Topaz Champion",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=5,
    clan=[UnicornClan],
    keywords=[Cavalry, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Saiken cannot gain Cavalry.<br><b>Home Engage, :bow::</b> Give <b>Reserve</b> to your target non-Unique Cavalry Personality in a Province."
Utaku_Saiken = Personality(
    card_id=11786,
    title="Utaku Saiken",
    force=0,
    chi=2,
    personal_honor=2,
    gold_cost=2,
    honor_requirement=None,
    clan=[UnicornClan],
    keywords=[Samurai, StableMaster],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
