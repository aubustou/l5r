from __future__ import annotations

from l5r_auto.clans import NinjaFaction, ScorpionClan, ShadowlandsFaction
from l5r_auto.keywords import (
    Air,
    BitterLies,
    Courtier,
    Duelist,
    Expendable,
    Experienced,
    Kensai,
    Kuroiban,
    Magistrate,
    Ninja,
    Resilient,
    Samurai,
    Shadowlands,
    Shugenja,
    Spy,
    Yojimbo,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<i>(Kensai may attach two One-Handed Weapons.)</i><br><b>Open, :g*::</b> Target a Weapon in your discard pile. Destroy one of Chiyoda's Madness tokens to Equip the Weapon to him."
Bayushi_Chiyoda = Personality(
    card_id=12476,
    title="Bayushi Chiyoda",
    force=2,
    chi=3,
    personal_honor=0,
    gold_cost=4,
    honor_requirement=None,
    clan=[ScorpionClan, ShadowlandsFaction],
    keywords=[Kensai, BitterLies, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Kanihime enters play, lose 1 Honor.<br><b>Ninja Open:</b> Kanihime has +1F/+1C while opposing another player's target Personality in a battle or duel. You may bow one of the target's attachments if he or she has a Poison token."
Bayushi_Kanihime = Personality(
    card_id=12477,
    title="Bayushi Kanihime",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Resilient, Ninja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Target an enemy Follower or Personality. Either give it -2F, or Fear 2 targeting it <i>(if legal)</i>. You may discard one of Shen-lao's Madness tokens to apply the effect you did not choose."
Bayushi_Shenlao = Personality(
    card_id=12478,
    title="Bayushi Shen-lao",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Kensai, Resilient, BitterLies, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Ninja Battle, :bow::</b> Melee 3 Attack. This will not be increased or combined, but may target a Personality with attached Followers and a Poison token."
Shosuro_Kayo_Experienced = Personality(
    card_id=12479,
    title="Shosuro Kayo",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=6,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Experienced("1"), Ninja, Samurai, Yojimbo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists. Draw a card after your Expendable card dies.)</i><br>After Ozu enters play, lose 4 Honor, or 2 Honor if you are Mantis Clan."
Shosuro_Ozu = Personality(
    card_id=12480,
    title="Shosuro Ozu",
    force=3,
    chi=3,
    personal_honor=0,
    gold_cost=2,
    honor_requirement=None,
    clan=[ScorpionClan, NinjaFaction],
    keywords=[Duelist, Expendable, Ninja, Spy],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear 2. If you have resolved an Honor action this turn, this Fear has +2 strength and may target a dishonorable Personality with Followers."
Yogo_Mizoguchi = Personality(
    card_id=12481,
    title="Yogo Mizoguchi",
    force=3,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[ScorpionClan],
    keywords=[Air, Courtier, Kuroiban, Magistrate, Shugenja],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
