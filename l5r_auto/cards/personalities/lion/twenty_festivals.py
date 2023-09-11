from __future__ import annotations

from l5r_auto.clans import LionClan
from l5r_auto.keywords import (
    Beastmaster,
    Cavalry,
    Commander,
    Conqueror,
    Daimyo,
    Deathseeker,
    Duelist,
    Experienced,
    Governor,
    Hero,
    Loyal,
    Paragon,
    Samurai,
    SoulOf,
    Tactician,
    Unique,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from ..common import Personality

"<b>Battle:</b> Fear equal to Eirasu's Force that bows any Undead card it targets. <i>(Target an enemy Follower or Personality without Followers; bow it if its Force is less than or equal to the Fear's strength.)</i>"
Akodo_Eirasu = Personality(
    card_id=12114,
    title="Akodo Eirasu",
    force=4,
    chi=3,
    personal_honor=0,
    gold_cost=7,
    honor_requirement=0,
    clan=[LionClan],
    keywords=[Deathseeker, Hero, Samurai, SoulOf("Akodo Ebiro")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :g2::</b> Discard a card to create a 2F Cat &#149; Nonhuman Follower and attach it to your target Beastmaster."
Akodo_Hio = Personality(
    card_id=12115,
    title="Akodo Hio",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=6,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Beastmaster, Samurai, SoulOf("Akodo Michio")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After your Personality wins a duel at a battlefield, give him +1F.<br><b>Iaijutsu Battle:</b> Kenaro challenges a target enemy Personality. Bow the loser."
Akodo_Kenaro_Experienced = Personality(
    card_id=12116,
    title="Akodo Kenaro",
    force=3,
    chi=4,
    personal_honor=4,
    gold_cost=9,
    honor_requirement=10,
    clan=[LionClan],
    keywords=[Duelist, Tactician, Unique, Experienced("1"), Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Your Bushido Virtue Strategies in and out of play have +1FV, to a maximum of 4."
Akodo_Naikiru = Personality(
    card_id=12117,
    title="Akodo Naikiru",
    force=3,
    chi=4,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Tactician, Governor, Samurai, SoulOf("Akodo Nakama")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>Shaido has +1F and +1PH while attacking."
Akodo_Shaido = Personality(
    card_id=12118,
    title="Akodo Shaido",
    force=1,
    chi=3,
    personal_honor=2,
    gold_cost=3,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br><b>Invest :g2::</b> Put an Iaijutsu Strategy in your discard pile into your hand. <i>(Entering play, permanently increase the Gold Cost by the Invest cost to get the effect.)</i>"
Akodo_Taiketsu = Personality(
    card_id=12119,
    title="Akodo Taiketsu",
    force=2,
    chi=4,
    personal_honor=3,
    gold_cost=5,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Battle: Discard a card to give this Tactician a Force bonus equal to the card's Focus Value.)</i> <br><b>Political Interrupt:</b> Before you gain Honor from a Battle action, negate the gain to draw a card."
Ikoma_Noritsu = Personality(
    card_id=12120,
    title="Ikoma Noritsu",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=5,
    clan=[LionClan],
    keywords=[Tactician, Samurai, SoulOf("Ikoma Tatsunori")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
Ikoma_Sairei = Personality(
    card_id=12121,
    title="Ikoma Sairei",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Paragon, Samurai, SoulOf("Ikoma Sido")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Fear 2, or Fear 4 if Ataruko has a Nonhuman, non-Shadowlands Follower."
Matsu_Ataruko = Personality(
    card_id=12122,
    title="Matsu Ataruko",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=4,
    clan=[LionClan],
    keywords=[Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Melee Attacks and Fear effects from Cat Followers in this army have +1 strength.<br><b>Interrupt:</b> After Chizuki enters play, search your Fate deck for Zaiko, show it, and put it in your hand."
Matsu_Chizuki = Personality(
    card_id=12123,
    title="Matsu Chizuki",
    force=4,
    chi=3,
    personal_honor=3,
    gold_cost=10,
    honor_requirement=8,
    clan=[LionClan],
    keywords=[Conqueror, Loyal, Unique, Beastmaster, Commander, Daimyo, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt:</b> Negate Iairimi's movement from the action."
Matsu_Iairimi = Personality(
    card_id=12124,
    title="Matsu Iairimi",
    force=3,
    chi=3,
    personal_honor=3,
    gold_cost=6,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Hero, Samurai, SoulOf("Matsu Mari")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Melee 3 Attack. Straighten Karoko if she is attacking."
Matsu_Karoko = Personality(
    card_id=12125,
    title="Matsu Karoko",
    force=3,
    chi=2,
    personal_honor=3,
    gold_cost=7,
    honor_requirement=7,
    clan=[LionClan],
    keywords=[Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br>Keiasu's Nonhuman, non-Shadowlands Followers have <b>Cavalry</b>."
Matsu_Keiasu = Personality(
    card_id=12126,
    title="Matsu Keiasu",
    force=2,
    chi=2,
    personal_honor=2,
    gold_cost=4,
    honor_requirement=6,
    clan=[LionClan],
    keywords=[Cavalry, Beastmaster, Commander, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Duelists win tied duels versus non-Duelists.)</i><br>After Seijuko wins a duel, give her +1PH.<br><b>Battle:</b> Fear equal to Seijuko's Personal Honor."
Matsu_Seijuko = Personality(
    card_id=12127,
    title="Matsu Seijuko",
    force=3,
    chi=3,
    personal_honor=2,
    gold_cost=5,
    honor_requirement=8,
    clan=[LionClan],
    keywords=[Duelist, Samurai],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
