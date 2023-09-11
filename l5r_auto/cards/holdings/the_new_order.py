from __future__ import annotations

from l5r_auto.keywords import (
    Expendable,
    Fortification,
    GeishaHouse,
    Imperial,
    Jade,
    Kharmic,
    Library,
    Market,
    Mine,
    Retainer,
    Shadowlands,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition

from .common import Holding

"<b>:bow::</b> Produce 3 Gold.<br><b>Tireless Open:</b> Discard a Kiho or a Spell to straighten this Holding. <i>(Tireless actions may be taken even while bowed.)</i>"
Contemplative_Shrine = Holding(
    card_id=11883,
    title="Contemplative Shrine",
    gold_cost=3,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"<b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Put a target Armor or Weapon in your discard pile into your hand. Destroy this Holding."
Delicate_Forge = Holding(
    card_id=11878,
    title="Delicate Forge",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"After this Holding enters play, give it three +1F Masterwork tokens.<br><b>:bow::</b> Produce 2 Gold.<br><b>Open, :bow::</b> Transfer a Masterwork token from this Holding to a target Armor or Weapon without a Masterwork token."
Developed_Quarry = Holding(
    card_id=11869,
    title="Developed Quarry",
    gold_cost=2,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold.<br><b>Battle/Open:</b> Give your target Monk or Shugenja +1F if he shares an element keyword with one of his Spells or your Rings."
Earthborn_Temple = Holding(
    card_id=11870,
    title="Earthborn Temple",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"This Fortification enters play bowed. Add 1 to the Honor required for an Honor Victory and -1 to the Honor required for a Dishonor Victory <i>(while this Holding is in play)</i>, or 2 and -2 respectively if you have Courtesy.<br><b>:bow::</b> Produce 2 Gold."
House_of_No_Tomorrow = Holding(
    card_id=11873,
    title="House of No Tomorrow",
    gold_cost=2,
    keywords=[Fortification, GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"Courtesy: After you Recruit this Holding from a Province, refill the Province face-up. <i>(Courtesy traits do not take effect if you went first.)</i><br><b>:bow::</b> Produce 4 Gold."
Jade_Bazaar = Holding(
    card_id=11874,
    title="Jade Bazaar",
    gold_cost=5,
    keywords=[Jade, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="4",
)
"After you Recruit this Holding, lose 1 Honor.<br><b>:bow::</b> Produce 2 Gold and lose 1 Honor."
Lane_of_Immorality = Holding(
    card_id=11880,
    title="Lane of Immorality",
    gold_cost=1,
    keywords=[Shadowlands],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"This Holding <i>(in and out of play)</i> has every non-boldface keyword on your face-up Holdings.<br><b>:bow::</b> Produce 2 Gold."
Missing_Caravan = Holding(
    card_id=11877,
    title="Missing Caravan",
    gold_cost=2,
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 5 Gold.<br><b>Political Tireless Interrupt:</b> Choose an Honor gain or loss from another player's action and reduce it to 2."
Otomo_Bureaucrat = Holding(
    card_id=11879,
    title="Otomo Bureaucrat",
    gold_cost=6,
    keywords=[Imperial, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="5",
)
"This Fortification enters play bowed.<br><b>:bow::</b> Produce 3 Gold. <br><b>Interrupt:</b> After you Recruit this Holding, look at the top three cards of your Fate deck. Place zero to two of them at the bottom of your deck."
Plain_Library = Holding(
    card_id=11875,
    title="Plain Library",
    gold_cost=3,
    keywords=[Expendable, Fortification, Library],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"<i>(Fortifications attach to the Province from which they entered play.)</i><br>This Fortification enters play bowed and, if your Sensei is Brotherhood Sensei, for 2 less Gold.<br><b>:bow::</b> Produce 4 Gold."
Protected_Temple = Holding(
    card_id=11871,
    title="Protected Temple",
    gold_cost=5,
    keywords=[Fortification, Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="4",
)
"<b>:bow::</b> Produce 1 Gold.<br><b>Open, :bow::</b> Search your Fate deck for a Ring. Show it. Put it into your hand. Discard a card. Destroy this Holding."
Remote_Temple = Holding(
    card_id=11881,
    title="Remote Temple",
    gold_cost=1,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="1",
)
"<b>:bow::</b> Produce 3 Gold.<br><b>Interrupt:</b> After you Recruit this Holding from a Province, look at the top three cards of your Dynasty deck. If one of them is a Mine, you may refill the Province with it, face-up."
Rich_Vein = Holding(
    card_id=11872,
    title="Rich Vein",
    gold_cost=3,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"Reduce all Honor losses from your cards by 1, to a minimum of 1.<br><b>:bow::</b> Produce 2 Gold."
Shrine_of_the_Colonies = Holding(
    card_id=11882,
    title="Shrine of the Colonies",
    gold_cost=2,
    keywords=[Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 1 Gold.<br><b>:bow::</b> Produce 2 Gold, which can only pay for a single Armor, Mine, or Weapon."
The_Toil_of_Zokujin = Holding(
    card_id=11868,
    title="The Toil of Zokujin",
    gold_cost=1,
    keywords=[Mine],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="1",
)
"<b>:bow::</b> Produce 6 Gold.<br><b>Open, :bow::</b> Create a +2F/+1C <b>One-Handed &#149; Sword &#149; Weapon</b> Item and attach it to your target Personality."
Weapon_Artist = Holding(
    card_id=11876,
    title="Weapon Artist",
    gold_cost=7,
    keywords=[Mine, Retainer],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="6",
)
