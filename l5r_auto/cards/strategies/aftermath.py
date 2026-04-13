from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import BushidoVirtue, Iaijutsu, Kata, Kharmic, Ninja, Political, Sincerity, Terrain
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Before this battle resolves, you may move one of your opposed attacking Personalities at this battlefield to an adjacent, unresolved battlefield.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
A_Moving_Battle = Strategy(card_id=10925, title='A Moving Battle', focus_value=3, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :g3::</b> Bow a target Personality. Lose 1 Honor.'
A_Small_Favor = Strategy(card_id=10926, title='A Small Favor', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Give your target opposed Personality +3F.'
A_Warriors_Brutality = Strategy(card_id=10927, title="A Warrior's Brutality", focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<b>Interrupt:</b> Negate an Event's effects."
Absolution = Strategy(card_id=10928, title='Absolution', focus_value=4, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Discipline :g2:. <i>(Pay 2 Gold to play, then remove from the game, this Discipline in your discard.)</i><br><b>Battle:</b> Give your target opposed Personality +2F.'
Banzai = Strategy(card_id=10929, title='Banzai!', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Open:</b> Destroy your target Holding. Give a Province +3 strength.'
Benediction = Strategy(card_id=10930, title='Benediction', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"As a Focus Effect, after you win this duel, gain 1 Honor and give the winner +1F.<br><b>Absent Battle:</b> Negate a target Personality's current Force bonuses or penalties <i>(you choose)</i>. <i>(Absent actions may be taken without presence.)</i>"
Breaking_the_Rhythm = Strategy(card_id=10931, title='Breaking the Rhythm', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Give <b>Reserve</b> to your target Personality in a Province. <i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i>'
Concealed_Reserves = Strategy(card_id=10932, title='Concealed Reserves', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Iaijutsu Political Limited:</b> Your target unbowed Personality challenges another player's target Personality. Each Personality must focus exactly once, if possible. The winner draws a card. Dishonor the loser."
Demonstrating_Technique = Strategy(card_id=10933, title='Demonstrating Technique', focus_value=4, keywords=[Iaijutsu, Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Political Open:</b> Bow your target unbowed Human Personality. Target another player's unbowed Human Personality. His controller may bow him and gain 1 Honor. If he did not choose this, dishonor both targets, and both their controllers lose 3 Honor."
Desire = Strategy(card_id=10934, title='Desire', focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :g4::</b> If there are any enemy units at this battlefield, search your Fate deck for a non-unique Battle Strategy. Show it and put it in your hand.'
Directing_the_Battle = Strategy(card_id=10935, title='Directing the Battle', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<b>Political Open:</b> Your target unbowed Human Personality commits seppuku. A target player loses Honor equal to the Personality's Personal Honor or 4, whichever is lower."
Dying_Remonstration = Strategy(card_id=10936, title='Dying Remonstration', focus_value=4, keywords=[BushidoVirtue, Political, Sincerity], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Give one or two target Gold-producing Holdings +1 Gold Production each <i>(this turn)</i>.'
Expanding_the_Gardens = Strategy(card_id=10937, title='Expanding the Gardens', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Discipline :g2: <i>(You may pay 2 Gold to play this Discipline from your discard pile, then remove it from the game after its action resolves.)</i><br><b>Battle:</b> Give this Province +2 or -2 Strength.'
Expensive_Achievement = Strategy(card_id=10938, title='Expensive Achievement', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Put this Kata into play. Discard all your other Kata in play.<br><b>Battle:</b> If this card is in play, straighten a Ring.'
Find_Your_Center = Strategy(card_id=10939, title='Find Your Center', focus_value=2, keywords=[Kharmic, Kata], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Give your target Personality with a Weapon +2F/+2C. If he is a Kensai, you may take an additional action.'
Grasp_the_Swords = Strategy(card_id=10940, title='Grasp the Swords', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'Attacking Personalities and Followers have -1F.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Hold_the_Walls = Strategy(card_id=10941, title='Hold the Walls', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"Discipline :g1: <i>(You may pay 1 Gold to play this Discipline from your discard pile, then remove it from the game after its action resolves.)</i><br><b>Limited, :g1::</b> Destroy one or two of a target Personality's tokens. Give him as many +1F tokens as the number of tokens this destroyed."
Knowledge_and_Power = Strategy(card_id=10942, title='Knowledge and Power', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Personalities without Followers have -2F. Commanders have +1F.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Lonely_Battlefield = Strategy(card_id=10943, title='Lonely Battlefield', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Engage:</b> Bow a target enemy attachment.'
Lost_Equipment = Strategy(card_id=10944, title='Lost Equipment', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Discipline :g1:. <i>(Pay 1 Gold to play, then remove from the game, this Discipline in your discard.)</i><br><b>Battle/Open:</b> Bow a target attachment.'
Lost_in_Transit = Strategy(card_id=10945, title='Lost in Transit', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Give your target Personality Force and Chi bonuses equal to his Personal Honor, minus 1 if he is unopposed.'
Marshal_Your_Strength = Strategy(card_id=10946, title='Marshal Your Strength', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Discipline :g1:. <i>(Pay 1 Gold to play, then remove from the game, this Discipline in your discard.)</i><br><b>Political Open:</b> Bow your target unbowed Courtier. The next two Honor losses from your cards <i>(this turn)</i> are increased by 1 each.'
Mercantile_Conflict = Strategy(card_id=10947, title='Mercantile Conflict', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Open, :g2::</b> If this Strategy is in your discard pile, put it into your hand before this phase ends.'
Move_the_Troops = Strategy(card_id=10948, title='Move the Troops', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle, :g5::</b> Discard a card to create a <b>Weapon</b> Item with a Force Modifier equal to the discarded card's Focus Value and attach it to your target Personality."
Never_Without_a_Weapon = Strategy(card_id=10949, title='Never Without a Weapon', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Ninja Limited</b>, :g10:: Destroy a target Personality with 3 or lower Chi, or with 4 or lower Chi if you control a Ninja Personality. Lose Honor equal to your Starting Family Honor.'
Planted_Evidence = Strategy(card_id=10950, title='Planted Evidence', focus_value=1, keywords=[Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Political Open, :gstar::</b> Bow your target unbowed Courtier. Destroy a target attachment with Gold Cost less than or equal to the amount of Gold paid, plus 3 if you control a Yojimbo.'
Provoked_Violence = Strategy(card_id=10951, title='Provoked Violence', focus_value=2, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"When Recruiting a Personality, if his Honor Requirement is higher than his owner's Family Honor, he costs 2 more Gold to Recruit.<br><b>Political Limited:</b> Put this Kata into play. Discard all your other Kata."
Respect = Strategy(card_id=10952, title='Respect', focus_value=4, keywords=[Kharmic, Kata, Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Discipline :g2: <i>(You may pay 2 Gold to play this Discipline from your discard pile, then remove it from the game after its action resolves.)</i><br><b>Absent Battle:</b> If you are the Defender, target your Personality at home and move him to this battlefield. After he moves, straighten him.'
Return_to_Action = Strategy(card_id=10953, title='Return to Action', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :g4::</b> Target your opposed Personality. Put a non-Unique Battle Strategy from your discard pile into your hand. If your Personality is a Magistrate, you may take an additional action.'
Sleight_of_Hand = Strategy(card_id=10954, title='Sleight of Hand', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"This Strategy's ability is Battle/Engage if you control a Scout at the current battlefield.<br><b>Battle:</b> A target enemy card may not use one of its abilities <i>(you choose)</i>."
Steal_an_Advantage = Strategy(card_id=10955, title='Steal an Advantage', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'As a Focus Effect, if you win this duel, draw a card.<br><b>Battle:</b> Move your target Personality home. You may target an enemy Personality and give him -3F.'
Strategic_Withdrawal = Strategy(card_id=10956, title='Strategic Withdrawal', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<i>(<b>Repeatable Limited, :g2::</b> Discard a Kharmic card to draw a card.)</i><br><b>Battle, :gstar::</b> Destroy a target enemy Follower or Weapon with Force less than or equal to the amount of Gold paid plus 2.'
Suffer_the_Consequences = Strategy(card_id=10957, title='Suffer the Consequences', focus_value=2, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 1 Attack.<br><b>Favor Political Battle:</b> Discard the Imperial Favor to make a Ranged 3 Attack.'
The_Legions_Might = Strategy(card_id=10958, title="The Legion's Might", focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Absent Battle:</b> If he would be opposed, move your target Personality at home to the current battlefield. If he is a Monk, give him +2F.'
The_Way_of_the_World = Strategy(card_id=10959, title='The Way of the World', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Target your unbowed Personality. Target an enemy unit with Force equal to or lower than your Personality's Force, or Force plus Personal Honor if he is defending. Destroy both targets."
Thoughtless_Sacrifice = Strategy(card_id=10960, title='Thoughtless Sacrifice', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Discipline :g2: <i>(You may pay the Discipline cost to play this card from the discard pile. Remove it from the game after the action resolves.)</i><br><b>Limited, :g1::</b> Give your target face-up Personality out of play <b>Destined</b>. <i>(Draw a card after your Destined card enters play.)</i>'
Two_Steady_Breaths = Strategy(card_id=10961, title='Two Steady Breaths', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Put this Kata into play. Discard all your other Kata in play with different titles.<br><b>Battle, :gstar::</b> If this card is in play, Equip a Spell to your target unbowed, opposed Shugenja. You may take an additional action.'
Unchecked_Fury = Strategy(card_id=10962, title='Unchecked Fury', focus_value=2, keywords=[Kata], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Melee 2 Attack.<br><b>Interrupt:</b> Give a Melee or Ranged Attack +2 strength.'
Unholy_Strike = Strategy(card_id=10963, title='Unholy Strike', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Give a target Personality a Force penalty equal to his printed Personal Honor. If he is dishonorable, bow him.'
Unpleasant_Truths = Strategy(card_id=10964, title='Unpleasant Truths', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Political Open:</b> Bow your target unbowed Courtier. All Personalities have -1F for each Clan Alignment in their army <i>(this turn)</i>.'
Unseemly_Alliance = Strategy(card_id=10965, title='Unseemly Alliance', focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])