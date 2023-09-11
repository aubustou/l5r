from __future__ import annotations

from l5r_auto.clans import MantisClan, ShadowlandsFaction
from l5r_auto.keywords import (
    Air,
    BountyHunter,
    Destined,
    Experienced,
    Fire,
    Kensai,
    Magistrate,
    Mercenary,
    Naval,
    Samurai,
    Scout,
    Shadowlands,
    Shugenja,
    Thunder,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Thunder Battle:</b> Fear 2, plus 1 for each Fire or Thunder action you have resolved from a Spell at this battlefield <i>(Bow a target enemy Follower or Personality without Followers with Force equal to or lower than the Fear's strength)</i>."
Moshi_Chiyoko = Personality(
    card_id=12464,
    title="Moshi Chiyoko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Fire, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once a turn, the Attacker gets the first Battle action, if it's from a Naval Personality's unit.)</i> <br>After Nariko Equips a Spell, give her +1F, and give her +1C if the Spell is Air or Thunder or you are Phoenix Clan."
Moshi_Nariko = Personality(
    card_id=12465,
    title="Moshi Nariko",
    force=2,
    chi=2,
    personal_honor=1,
    gold_cost=4,
    honor_requirement=None,
    clan=[MantisClan],
    keywords=[Naval, Air, Shugenja, Thunder],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Compassion: Instead of drawing a card for bringing Kinuyo into play, you may put a card in your Fate discard pile into your hand. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i>"
Tsuruchi_Kinuyo = Personality(
    card_id=12466,
    title="Tsuruchi Kinuyo",
    force=3,
    chi=2,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=2,
    clan=[MantisClan],
    keywords=[Destined, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Ranged 3 Attack. If this destroyed an enemy Personality, move Taito home; this movement is optional if the Defender has taken an action this battle."
Tsuruchi_Taito_Experienced = Personality(
    card_id=12467,
    title="Tsuruchi Taito",
    force=4,
    chi=3,
    personal_honor=2,
    gold_cost=8,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Naval, BountyHunter, Experienced("1"), Magistrate, Samurai, Scout],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Your Peasant Weapons out of play have <b>Honor</b>. <i>(Repeatable Interrupt: Discard an Honor card to give an Honor gain or loss +1 or -1.)</i><br><b>Battle:</b> Target Honjo's Weapon. Bow it, or if it is a Peasant Weapon you may destroy it, to make a Melee 2 Attack."
Yoritomo_Honjo = Personality(
    card_id=12468,
    title="Yoritomo Honjo",
    force=3,
    chi=3,
    personal_honor=1,
    gold_cost=5,
    honor_requirement=0,
    clan=[MantisClan],
    keywords=[Kensai, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After Tamiya enters play, lose 2 Honor. Your Peasant Weapons out of play have <b>Courage</b>. <i>(Repeatable Interrupt: Discard a Courage card to give a Fear effect +2 or -2 strength.)</i>"
Yoritomo_Tamiya = Personality(
    card_id=12469,
    title="Yoritomo Tamiya",
    force=4,
    chi=2,
    personal_honor=0,
    gold_cost=5,
    honor_requirement=None,
    clan=[MantisClan, ShadowlandsFaction],
    keywords=[Kensai, Naval, Mercenary, Samurai, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
