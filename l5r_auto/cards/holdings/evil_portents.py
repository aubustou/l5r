from __future__ import annotations

from l5r_auto.keywords import (
    Destined,
    Dojo,
    Expendable,
    Experienced,
    Fortification,
    Kharmic,
    Library,
    Nonhuman,
    Oni,
    Retainer,
    Shadowlands,
    Temple,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

"<b>Battle, :bow::</b> Straighten your target Spell. You may use its abilities a second time this turn, but they do not give Force bonuses to unopposed Personalities."
City_of_Night_Experienced = Holding(
    card_id=12424,
    title="City of Night",
    gold_cost=1,
    keywords=[Experienced("1"), Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"You may take this Holding's actions during a battle at any battlefield where you control a Siege Personality. <br><b>Battle, :bow::</b> Ranged 2 Attack. <br><b>Interrupt, :bow::</b> Give the action's Ranged Attacks +2 strength."
Defensive_Fortification = Holding(
    card_id=12425,
    title="Defensive Fortification",
    gold_cost=3,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"You may Recruit this Holding as an Open. <br>After you Recruit this Holding, you may target and straighten a Duelist."
Dojo_of_the_Dauntless = Holding(
    card_id=12426,
    title="Dojo of the Dauntless",
    gold_cost=2,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding enters play unbowed if you control any Siege Personalities.<br><b>Open, :bow::</b> If you control any Personalities, gain 1 Honor."
Erected_Watchtower = Holding(
    card_id=12427,
    title="Erected Watchtower",
    gold_cost=2,
    keywords=[Expendable, Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After a Kharmic action puts this Holding into a discard pile, draw a card and remove this Holding from the game.<br>This Holding has +1GP when it pays for a single Kharmic action only."
KiRins_Shrine_Experienced_2 = Holding(
    card_id=12428,
    title="Ki-Rin's Shrine",
    gold_cost=1,
    keywords=[Experienced("2"), Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action Equips a Spell from your hand, draw a card. You may not use abilities on any Libraries of Kyuden Isawa again this turn."
Libraries_of_Kyuden_Isawa = Holding(
    card_id=12429,
    title="Libraries of Kyuden Isawa",
    gold_cost=6,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding enters play for 1 less Gold if another of your Dojos entered play this turn."
Master_of_Clear_Water_Dojo = Holding(
    card_id=12430,
    title="Master of Clear Water Dojo",
    gold_cost=3,
    keywords=[Dojo, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding has +1GP when it pays to Recruit or Equip a single Library or Spell only."
Retired_Scholar = Holding(
    card_id=12431,
    title="Retired Scholar",
    gold_cost=2,
    keywords=[Kharmic, Library, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle/Open, :bow::</b> Target your Duelist who has not been targeted by a Shadowless Strike Dojo this turn. Your Duelist has +1F while opposed. After he or she enters a duel facing a Personality with higher Chi, give your Duelist +1C in the duel's resolution."
Shadowless_Strike_Dojo = Holding(
    card_id=12432,
    title="Shadowless Strike Dojo",
    gold_cost=1,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Give a target enemy Follower or Personality -2F. If the target is Shadowlands and attacking, give it -4F instead and bow it if its Force is now 0."
Shinseis_Last_Hope_Experienced = Holding(
    card_id=12433,
    title="Shinsei's Last Hope",
    gold_cost=4,
    keywords=[Experienced("1")],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After this Holding enters play from a Province, refill the Province face-up."
Spirits_Essence_Dojo = Holding(
    card_id=12434,
    title="Spirit's Essence Dojo",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> Give one of the action's Fear effects +1 strength."
Temple_of_the_First_Seal = Holding(
    card_id=12435,
    title="Temple of the First Seal",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After this Holding enters play, lose 3 Honor. This Holding enters play for 1 less Gold for each Shadowlands Follower and Personality you control. After you bow this Holding, lose 1 Honor.<br><b>Open, :bow::</b> Straighten your target Oni."
The_Feeding_Hills = Holding(
    card_id=12436,
    title="The Feeding Hills",
    gold_cost=3,
    keywords=[Nonhuman, Oni, Shadowlands],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Draw a card after you Recruit a Destined card.)</i><br>After you draw a card for bringing this Holding into play, if you then have four or more cards in your hand, discard a card."
The_Ikoma_Halls = Holding(
    card_id=12437,
    title="The Ikoma Halls",
    gold_cost=3,
    keywords=[Destined, Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open:</b> Once per game, create and attach a +2F/+1C One-<b>Handed &#149; Sword &#149; Weapon</b> Item to your target Duelist."
The_Iron_Mountain_School = Holding(
    card_id=12438,
    title="The Iron Mountain School",
    gold_cost=6,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :bow::</b> Transfer your target Spell <i>(in play)</i> to your target Shugenja."
The_Miya_Records = Holding(
    card_id=12439,
    title="The Miya Records",
    gold_cost=2,
    keywords=[Library],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
