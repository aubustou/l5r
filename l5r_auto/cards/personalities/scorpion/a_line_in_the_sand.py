from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    Air,
    Cavalry,
    Conqueror,
    Courtier,
    Ninja,
    Reserve,
    Resilient,
    Samurai,
    Scout,
    Shugenja,
    Yojimbo,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from ..common import Personality

"Atsuto has <b>Resilient</b> while opposing a dishonorable Personality. <i>(Once per game per card, a Resilient card does not die in battle resolution.)</i>"
Bayushi_Atsuto = Personality(
    card_id=11598,
    title="Bayushi Atsuto",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Conqueror, Courtier, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Home Battle:</b> If he would be opposed, move Yasunari to the current battlefield."
Bayushi_Yasunari = Personality(
    card_id=11599,
    title="Bayushi Yasunari",
    force=3,
    chi=1,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br>Kiyofumi has Destined while you control a Geisha <i>(Geisha Houses are not Geisha; Draw a card after you Recruit a Destined card)</i>."
Shosuro_Kiyofumi = Personality(
    card_id=11600,
    title="Shosuro Kiyofumi",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Resilient, Ninja, Scout],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt:</b> Increase each Honor loss from the Battle action by 1."
Shosuro_Yasumasa = Personality(
    card_id=11601,
    title="Shosuro Yasumasa",
    force=1,
    chi=4,
    personal_honor=1,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action Equips your Spell to Kitaiko, draw a card. <br><b>Air Tireless Open:</b> If Kitaiko has an Air Spell, straighten her."
Soshi_Kitaiko = Personality(
    card_id=11602,
    title="Soshi Kitaiko",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Courtier, Shugenja],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
'Gingo enters play for 1 less Gold if your Allegiance is Traditionalist.<br>Invest :g10:: Give Gingo two +1F/+1C tokens, and permanently give him <b>Conqueror </b>and the ability, "<b>Battle:</b> Move a target Personality home." This Invest cost cannot be reduced.'
Yogo_Gingo = Personality(
    card_id=11603,
    title="Yogo Gingo",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Cavalry, Reserve, Samurai],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
