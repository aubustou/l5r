from __future__ import annotations

from l5r_auto.keywords import (
    Barrack,
    Barracks,
    Dojo,
    Farm,
    Fortification,
    Retainer,
    Winter,
)
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition

from .common import Holding

"<i>(Fortifications attach to the Province from which they entered play.)</i> <br>If you use this Holding's Gold Production to Recruit a single Fortification only, you choose which of your Provinces the Fortification attaches to."
Architect = Holding(
    card_id=12268,
    title="Architect",
    gold_cost=3,
    gold_production="3",
    keywords=[Fortification, Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Courtesy: This Holding also straightens at the start of other players' turns, but has -1GP on those turns. <i>(Courtesy traits do not take effect if you went first.)</i>"
Ashigaru_Farmland = Holding(
    card_id=12269,
    title="Ashigaru Farmland",
    gold_cost=3,
    gold_production="3",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding has +1GP when it pays to Recruit a single Farm only, or when it pays for a single Sensei action only."
Bamboo_Irrigation = Holding(
    card_id=12270,
    title="Bamboo Irrigation",
    gold_cost=1,
    gold_production="1*",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Interrupt, :bow::</b> After the action Recruits an Ashigaru Personality, create a 0F/1C/0PH <b>Ashigaru &#149; Conscript</b> Personality. Destroy this Holding."
Borderless_Fields = Holding(
    card_id=12271,
    title="Borderless Fields",
    gold_cost=2,
    gold_production="2",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle, :bow::</b> Give your target opposed Follower +1F, or +2F if it is attached to a Commander."
Combat_Drill_Field = Holding(
    card_id=12272,
    title="Combat Drill Field",
    gold_cost=1,
    gold_production="1",
    keywords=[Barrack],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"You have +1 maximum hand size."
Daikura = Holding(
    card_id=12273,
    title="Daikura",
    gold_cost=3,
    gold_production="3",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle:</b> Transfer your target Follower from your target Personality to your other target Personality."
Garrison_Hub = Holding(
    card_id=12274,
    title="Garrison Hub",
    gold_cost=2,
    gold_production="2",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"Courtesy: Your Provinces have +1 strength. <i>(Courtesy traits do not take effect if you went first.)</i>"
Hasty_Defenses = Holding(
    card_id=12275,
    title="Hasty Defenses",
    gold_cost=2,
    gold_production="2",
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :bow::</b> Put a target Follower in your discard pile into your hand."
Heisha = Holding(
    card_id=12276,
    title="Heisha",
    gold_cost=6,
    gold_production="5",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After this Holding enters play, create a 0F/1C/0PH <b>Ashigaru &#149; Conscript</b> Personality and straighten your Sensei."
Isolated_Farmlands = Holding(
    card_id=12277,
    title="Isolated Farmlands",
    gold_cost=6,
    gold_production="5",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"This Holding has +1GP for each different title among your Barracks Holdings, other than Mess Hall, maximum +2GP."
Mess_Hall = Holding(
    card_id=12278,
    title="Mess Hall",
    gold_cost=3,
    gold_production="2*",
    keywords=[Barracks],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Tireless Interrupt, :g*::</b> If you bowed this Holding to produce Gold while Recruiting a Commander, Equip a target Follower to him from your hand for 1 less Gold after he enters play."
Officers_Lodge = Holding(
    card_id=12279,
    title="Officer's Lodge",
    gold_cost=3,
    gold_production="3",
    keywords=[Barracks, Winter],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Open, :bow::</b> Draw a card. If you now have more cards in your hand than each other player, discard a card. Destroy this Holding."
Padis_Dojo = Holding(
    card_id=12280,
    title="Padis Dojo",
    gold_cost=2,
    gold_production="2",
    keywords=[Dojo],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<i>(Fortifications attach to the Province from which they entered play.)</i> <br>After this Holding is destroyed, gain 2 Honor."
Peaceful_Retreat = Holding(
    card_id=12281,
    title="Peaceful Retreat",
    gold_cost=4,
    gold_production="4",
    keywords=[Fortification],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"After this Holding enters play, a target player gains or loses 1 Honor."
Rhetorician = Holding(
    card_id=12282,
    title="Rhetorician",
    gold_cost=3,
    gold_production="3",
    keywords=[Retainer],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
"<b>Battle/Open:</b> Straighten your target Ashigaru Follower."
Veterans_Farmland = Holding(
    card_id=12283,
    title="Veteran's Farmland",
    gold_cost=2,
    gold_production="2",
    keywords=[Farm],
    traits=[],
    abilities=[],
    legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition],
)
