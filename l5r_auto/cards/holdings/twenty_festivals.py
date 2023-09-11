from __future__ import annotations

from l5r_auto.keywords import (
    Barracks,
    Destined,
    Dojo,
    Expendable,
    Fortification,
    Kharmic,
    Legacy,
    Library,
    Market,
    Port,
    Temple,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

"<i>(Draw a card after your Expendable card is destroyed. Fortifications attach, bowed, to the Province from which they entered play.)</i> <br><b>Tireless Interrupt:</b> Negate all the action's Melee and Ranged Attacks <i>(at this battlefield)</i>."
Blessed_Herbalist = Holding(
    card_id=12068,
    title="Blessed Herbalist",
    gold_cost=2,
    gold_production="2",
    keywords=[Expendable, Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Fortifications attach, bowed, to the Province from which they entered play.)</i><br>Before this Province is destroyed, transfer this Holding to an adjacent Province.<br><b>Tireless Open:</b> Straighten this Holding. It will not produce Gold until after your next turn begins."
Distracted_Sentries = Holding(
    card_id=12069,
    title="Distracted Sentries",
    gold_cost=6,
    gold_production="5",
    keywords=[Fortification, Kharmic],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow:, :g*::</b> Equip a target Spell to your target opposed, unbowed Shugenja, paying 2 less Gold. If he and the Spell share an element or Thunder keyword, you may take an additional action from the Spell."
Elemental_Library = Holding(
    card_id=12070,
    title="Elemental Library",
    gold_cost=2,
    gold_production="2",
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Once per turn as a <b>Dynasty</b>, remove a card in your hand from the game to search your deck and Provinces for a Legacy Holding and Recruit it.)</i> <br>You must have at least 16 Holdings in your deck construction."
Forgotten_Legacy = Holding(
    card_id=12071,
    title="Forgotten Legacy",
    gold_cost=3,
    gold_production="3",
    keywords=[Legacy],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow:, :g*::</b> Equip a target Follower or Spell in your discard pile if another player's action destroyed it or its Personality this battle."
Forward_Encampment = Holding(
    card_id=12072,
    title="Forward Encampment",
    gold_cost=2,
    gold_production="2",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding enters play unbowed.<br><b>Interrupt, :bow::</b> Negate an Engage action.<br><b>Battle, :bow::</b> Ranged 3 Attack."
KaiuBuilt_Defenses = Holding(
    card_id=12073,
    title="Kaiu-Built Defenses",
    gold_cost=0,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
    gold_production=None,
)
"<i>(Fortifications attach, bowed, to the Province from which they entered play.)</i> <br><b>Interrupt, :bow::</b> Negate the movement into an attacking army of a target Personality at any location."
Labor_Crew = Holding(
    card_id=12074,
    title="Labor Crew",
    gold_cost=2,
    gold_production="2",
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Tireless Interrupt:</b> If you have won a duel this turn, each of the action's Fear effects have +1 strength and may target Items and Spells. <i>(Tireless actions may be taken even while bowed.)</i>"
Personal_Dojo = Holding(
    card_id=12075,
    title="Personal Dojo",
    gold_cost=3,
    gold_production="3",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Invest :g2:: Give this Holding two +1GP Wealth tokens. <i>(Entering play, permanently increase the Gold Cost by the Invest cost to get the effect.)</i>"
Questionable_Market = Holding(
    card_id=12076,
    title="Questionable Market",
    gold_cost=1,
    gold_production="1",
    keywords=[Market, Port],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> Bow the winner of any duel created by the action if he was the challenger. Destroy this Holding."
Secret_Dojo = Holding(
    card_id=12077,
    title="Secret Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card.)</i>"
Temple_of_Destiny = Holding(
    card_id=12078,
    title="Temple of Destiny",
    gold_cost=1,
    gold_production="1",
    keywords=[Destined, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
'<b>Interrupt, :bow::</b> If the action creates a duel, then after your Personality wins it permanently give him the ability, "<b>Battle:</b> Fear 4 <i>(Bow a target enemy Follower or Personality without Followers with 4 or lower Force)</i>." Destroy this Holding.'
The_Obsidian_Dojo = Holding(
    card_id=12079,
    title="The Obsidian Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :bow::</b> Straighten your target Personality. Destroy this Holding.<br><b>Open, :bow::</b> Straighten this Holding if you have not given any Madness tokens this turn. Give a target Personality a <b>Madness </b>token."
Throes_of_Madness = Holding(
    card_id=12080,
    title="Throes of Madness",
    gold_cost=2,
    gold_production="2",
    keywords=[Kharmic],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
