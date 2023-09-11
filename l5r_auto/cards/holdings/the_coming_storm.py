from __future__ import annotations

from l5r_auto.keywords import (
    Dojo,
    Farm,
    Fortification,
    Imperial,
    Kharmic,
    Market,
    Merchant,
    Retainer,
    SakeHouse,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

"<b>:bow::</b> Produce 2 Gold<br><b>Open, :bow::</b> Increase a positive numeral on your target Spell by 1. <i>(2 is a numeral, two is not.)</i>"
Alchemy_Lab = Holding(
    card_id=11712,
    title="Alchemy Lab",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition],
)
"<b>:bow::</b> Produce 1 Gold. Give this Holding a +1 Gold Production <b>Wealth </b>token if you are bringing a Holding into play."
Bookkeeper = Holding(
    card_id=11713,
    title="Bookkeeper",
    gold_cost=1,
    keywords=[Merchant, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 4 Gold.<br><b>Battle, :bow::</b> Target two or more of your Personalities with Force penalties from the same source. Negate those penalties."
Bountiful_Fields = Holding(
    card_id=11714,
    title="Bountiful Fields",
    gold_cost=4,
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Fortifications attach to the Province from which they entered play.)</i><br>This Fortification enters play bowed.<br><b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Gain 1 Honor."
Carpenter_Shrine = Holding(
    card_id=11715,
    title="Carpenter Shrine",
    gold_cost=2,
    keywords=[Fortification, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i><br><b>:bow::</b> Produce 5 Gold."
Cloth_Market = Holding(
    card_id=11716,
    title="Cloth Market",
    gold_cost=5,
    keywords=[Kharmic, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(Fortifications attach to the Province from which they entered play.)</i><br>This Fortification enters play bowed. This Province has +2 strength.<br><b>:bow::</b> Produce 2 Gold."
Defensive_Memorial = Holding(
    card_id=11717,
    title="Defensive Memorial",
    gold_cost=2,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 3 Gold.<br><b>Interrupt, :bow::</b> Give a Ranged Attack +1 strength."
Expansive_Range = Holding(
    card_id=11718,
    title="Expansive Range",
    gold_cost=3,
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 5 Gold. <br><b>Battle:</b> Straighten your target Personality. Bow him before this battle resolves."
Hoteis_Smile = Holding(
    card_id=11719,
    title="Hotei's Smile",
    gold_cost=6,
    keywords=[SakeHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"After this Holding enters play, lose 3 Honor.<br><b>:bow::</b> Produce 2 Gold, or lose 1 Honor to produce 3 Gold.<br><b>Tireless Open:</b> Give another player's target Personality -2PH."
House_of_Disgrace = Holding(
    card_id=11720,
    title="House of Disgrace",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 2 Gold.<br><b>Battle/Open:</b> Transfer your target Fortification at any Province to any of your other Provinces."
Kaiu_Engineers = Holding(
    card_id=11721,
    title="Kaiu Engineers",
    gold_cost=2,
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"You are considered to have +5 Family Honor when Lobbying checks Honor.<br><b>:bow::</b> Produce 1 Gold.<br><b>Open, :bow::</b> Straighten a target Personality who Lobbied this turn."
Shigekawas_Court = Holding(
    card_id=11722,
    title="Shigekawa's Court",
    gold_cost=1,
    keywords=[Imperial, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 3 Gold.<br><b>Open, :bow::</b> Straighten a target Sensei."
Summer_Court = Holding(
    card_id=11723,
    title="Summer Court",
    gold_cost=3,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>:bow::</b> Produce 2 Gold.<br><b>Battle, :gstar:, :bow::</b> Equip a Spell to your target opposed Shugenja for 2 less Gold. Gain 1 Honor, or 2 Honor if the target is defending."
Temple_of_Serenity = Holding(
    card_id=11724,
    title="Temple of Serenity",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"Invest :g1:: Until the game ends, this Holding also straightens at the start of other players' turns. <i>(After this card enters play, you may also pay the Invest cost to get the effect.)</i><br><b>:bow::</b> Produce 2 Gold."
Temple_of_the_Heavenly_Crab = Holding(
    card_id=11725,
    title="Temple of the Heavenly Crab",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Move your target Personality home.<br><b>Absent Battle, :bow::</b> Move your target Personality at home to this battlefield."
Tunnel_Network = Holding(
    card_id=11726,
    title="Tunnel Network",
    gold_cost=0,
    keywords=[Fortification, Kharmic],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
"<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i><br><b>:bow::</b> Produce 3 Gold.<br><b>Interrupt:</b> After each time the action discards or shows any cards, you may give them +1FV. <i>(Focused cards cannot gain this bonus.)</i>"
Voice_of_Experience = Holding(
    card_id=11727,
    title="Voice of Experience",
    gold_cost=3,
    keywords=[Kharmic, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
)
