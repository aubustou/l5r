from __future__ import annotations

from l5r_auto.abilities import Ability
from l5r_auto.cards import Entity
from l5r_auto.keywords import (
    Dojo,
    Fortification,
    GeishaHouse,
    Imperial,
    Kharmic,
    Market,
    Port,
    SakeHouse,
    Temple,
)
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
from l5r_auto.play import Game
from l5r_auto.player import Player
from l5r_auto.utils import is_entity_of_type

from .common import Holding

"Your minimum Dynasty deck size is increased by two.<br><b>:bow::</b> Produce 5 Gold."
Coastal_Lane = Holding(
    card_id=11547,
    title="Coastal Lane",
    gold_cost=4,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="5",
)
"This Holding enters play for 2 less Gold if you control any Port Holdings.<br><b>:bow::</b> Produce 3 Gold.<br>Once per turn, produce 1 Gold that can only pay for a single action from your card in play."
Colonial_Market = Holding(
    card_id=11548,
    title="Colonial Market",
    gold_cost=5,
    keywords=[Kharmic, Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"<b>:bow::</b> Produce 2 Gold. <br><b>Economic Open, :g2::</b> Choose a player with three or more Holdings in play. Give his target Holding -2GP <i>(this turn)</i>."
Contested_Market = Holding(
    card_id=11549,
    title="Contested Market",
    gold_cost=2,
    keywords=[Market, Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i> <br>This Holding enters play for 1 less Gold for each Geisha <i>(not Geisha House)</i> you control.<br><b>:bow::</b> Produce 3 Gold."
Hanamachi = Holding(
    card_id=11550,
    title="Hanamachi",
    gold_cost=4,
    keywords=[Kharmic, GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
'<b>:bow::</b> Produce 3 Gold.<br><b>Open, :bow::</b> Create a 0F/1C/0PH Geisha Personality under another player\'s control with the trait "You have -1 maximum hand size." Destroy this Holding.'
House_of_Floating_Petals = Holding(
    card_id=11551,
    title="House of Floating Petals",
    gold_cost=3,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"<b>:bow::</b> Produce 5 Gold. <br>After a Personality is Recruited, you may bow and destroy this Holding to bow him, and you gain a Conspiracy token if his controller has no unbowed Personalities in play."
House_of_Loose_Silk = Holding(
    card_id=11552,
    title="House of Loose Silk",
    gold_cost=6,
    keywords=[GeishaHouse, SakeHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="5",
)


class HouseOfTheFloatingLotusAbility(Ability):
    "<b>:bow::</b> Produce 2 Gold, or 4 Gold if you control two or more other Geisha Houses."

    gold_amount: int = 2

    def on_pay(self, game: Game, player: Player, entity: Entity) -> int:
        if len([x for x in player.play_area if is_entity_of_type(x, GeishaHouse)]) >= 2:
            return self.gold_amount + 2
        else:
            return self.gold_amount


House_of_the_Floating_Lotus = Holding(
    card_id=11553,
    title="House of the Floating Lotus",
    gold_cost=3,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[HouseOfTheFloatingLotusAbility()],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 2 Gold.<br><b>:bow::</b> Produce 2 Gold that can only pay for a single Kharmic action. Straighten this Holding after your next Dynasty Phase begins."
Kumite_Grounds = Holding(
    card_id=11554,
    title="Kumite Grounds",
    gold_cost=2,
    keywords=[Kharmic, Temple],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card from your Province and refill it face-up.)</i> <br>After you Equip a Follower paying 1 or more Gold, give this Holding +1GP <i>(this turn)</i>.<br><b>:bow::</b> Produce 2 Gold."
Lonely_Dojo = Holding(
    card_id=11555,
    title="Lonely Dojo",
    gold_cost=2,
    keywords=[Kharmic, Dojo],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 1 Gold.<br><b>Open, :bow::</b> A target player shows a random card in his hand.<br><b>Open, :bow::</b> Turn a target card in another player's Province face-up."
Momijis_Chambers = Holding(
    card_id=11556,
    title="Momiji's Chambers",
    gold_cost=1,
    keywords=[GeishaHouse],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="1",
)
"This Fortification enters play bowed. This Province has +1 strength for each other Fortification attached to it, up to 3.<br><b>:bow::</b> Produce 3 Gold."
MushaGaeshi = Holding(
    card_id=11557,
    title="Musha-Gaeshi",
    gold_cost=3,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="3",
)
"<b>:bow::</b> Produce 2 Gold.<br>You may use this Holding's printed ability one additional time per turn for each of your Markets in play. <br><b>Economic Battle, :g2::</b> Give a target enemy Personality -1F."
Second_City_Harbor = Holding(
    card_id=11558,
    title="Second City Harbor",
    gold_cost=2,
    keywords=[Port],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"<b>:bow::</b> Produce 1 Gold.<br><b>Open, :bow:, :gstar::</b> Search your Dynasty deck for a Market or Port. Recruit it <i>(bowed)</i>. Destroy this Holding."
Second_City_Market = Holding(
    card_id=11559,
    title="Second City Market",
    gold_cost=1,
    keywords=[Market],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="1",
)
"This Fortification enters play bowed. Your Fear effects during battles at this Province have +1 strength.<br><b>:bow::</b> Produce 2 Gold."
The_Inner_Ring = Holding(
    card_id=11560,
    title="The Inner Ring",
    gold_cost=2,
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
"After this Holding enters play, take the Imperial Favor and rehonor one of your Personalities <i>(if able)</i>. You may Recruit this Holding as a <b>Political Open</b> action.<br><b>:bow::</b> Produce 2 Gold."
The_Ivory_Courtroom = Holding(
    card_id=11561,
    title="The Ivory Courtroom",
    gold_cost=2,
    keywords=[Imperial],
    traits=[],
    abilities=[],
    legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition, ModernEdition],
    gold_production="2",
)
