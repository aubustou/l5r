from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import (
    Air,
    Alchemist,
    BitterLies,
    Courtier,
    Duelist,
    Experienced,
    Intimidator,
    Kensai,
    Loyal,
    Ninja,
    PoisonMaster,
    Samurai,
    Seductress,
    Shugenja,
    SoulOf,
    Unique,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Political Interrupt:</b> If the action targets Junko and is another player's, he may choose to lose 2 Honor. If he did not choose this, negate the action.<br><b>Tireless Battle:</b> Move Junko home."
Bayushi_Junko = Personality(
    card_id=12151,
    title="Bayushi Junko",
    force=0,
    chi=4,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Courtier, Intimidator, SoulOf("Bayushi Jou")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Political Interrupt:</b> After Katsue enters play, a target player loses 1 Honor."
Bayushi_Katsue = Personality(
    card_id=12152,
    title="Bayushi Katsue",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Courtier, Samurai, SoulOf("Bayushi Shigeru")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons.)</i>"
Bayushi_Manora = Personality(
    card_id=12153,
    title="Bayushi Manora",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Kensai may attach two One-Handed Weapons.)</i><br><b>Battle, :bow::</b> Fear 4. You may bow Saikaku's Weapon or destroy a Madness token on him to straighten him."
Bayushi_Saikaku = Personality(
    card_id=12154,
    title="Bayushi Saikaku",
    force=3,
    chi=2,
    personal_honor=1,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Sunetsu's Items must be Armor or Weapons.<br><b>Battle:</b> If Sunetsu has one or no Followers, move her to an unresolved battlefield."
Bayushi_Sunetsu = Personality(
    card_id=12155,
    title="Bayushi Sunetsu",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=7,
    honor_requirement=0,
    clan=[ScorpionClan],
    keywords=[Samurai, SoulOf("Bayushi Sunetra")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear equal to the Force of your target unbowed Kensai. You may destroy a Madness token on Toshimo to have this destroy cards after it bows them."
Bayushi_Toshimo_Experienced = Personality(
    card_id=12156,
    title="Bayushi Toshimo",
    force=4,
    chi=3,
    personal_honor=1,
    gold_cost=9,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, Unique, BitterLies, Experienced("1"), Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>Longji's Followers must be Ninja. Personalities cannot refuse a challenge from Longji unless they bow first. Your actions targeting Longji that create challenges are Unstoppable. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Shosuro_Longji = Personality(
    card_id=12157,
    title="Shosuro Longji",
    force=2,
    chi=5,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Ninja, SoulOf("Shosuro Aroru")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>After Saigyo enters play, lose 2 Honor.<br><b>Ninja Battle:</b> A target enemy Personality challenges Saigyo. Give the winner +2F."
Shosuro_Saigyo = Personality(
    card_id=12158,
    title="Shosuro Saigyo",
    force=2,
    chi=2,
    personal_honor=0,
    gold_cost=3,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Ninja Open, :bow::</b> Your other target unbowed Ninja Personality challenges another player's target Personality. He may refuse; if he does, give him a -1F/-1C Poison token. Bow the loser."
Shosuro_Sakura = Personality(
    card_id=12159,
    title="Shosuro Sakura",
    force=3,
    chi=4,
    personal_honor=0,
    gold_cost=8,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Loyal, Unique, Alchemist, Ninja, PoisonMaster, Seductress],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After an action from Rei's unit dishonors another player's Personality, his controller loses 1 Honor. After the first time each turn her own Spell bows Rei, straighten her."
Soshi_Rei = Personality(
    card_id=12160,
    title="Soshi Rei",
    force=0,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
