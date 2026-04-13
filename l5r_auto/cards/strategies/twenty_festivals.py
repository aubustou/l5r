from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Courage, Kata, Kharmic
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'This ability has Absent if it targets a Cavalry card or if you ever had presence at this battlefield. <i>(Absent actions may be taken without presence.)</i><br><b>Battle:</b> Give a target enemy Follower or Personality -3F.'
Alliance_Threatened = Strategy(card_id=12220, title='Alliance Threatened', focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle/Engage, :g*::</b> Equip a target Weapon from your hand to your target opposed Personality. If he is a Kensai, draw a card after it attaches.'
Art_of_the_Iai = Strategy(card_id=12221, title='Art of the Iai', focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Iaijutsu Battle:</b> Your target unbowed Personality challenges a target enemy Personality. Bow the loser. If your Personality is a Duelist and you won the duel by three or more, you may take an additional action.'
Brazen_Challenge = Strategy(card_id=12222, title='Brazen Challenge', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Open:</b> Put this Kata into play. Discard your other Kata in play.<br><b>Interrupt, :bow::</b> The action's Ranged Attacks bow, instead of destroying, Personalities with Spells."
Brush_The_Arrow_Aside = Strategy(card_id=12223, title='Brush The Arrow Aside', focus_value=1, keywords=[Courage, Kata], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Dynasty, :g*::</b> Search your Dynasty deck for a non-Unique Holding and Recruit it, paying 1 more Gold unless it is a Fortification. <i>(You may only take Dynasty actions during your Dynasty Phase.)</i>'
Building_Contract = Strategy(card_id=12224, title='Building Contract', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Iaijutsu Open:</b> Your target unbowed Personality challenges a target Personality. Dishonor and permanently remove all abilities from the loser. The winner gains 1 Honor.'
Clash_of_Blades = Strategy(card_id=12225, title='Clash of Blades', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Interrupt:</b> Each of the action's Melee and Ranged Attacks has -1 strength, or -3 strength if its target has Armor attached.<br><b>Open:</b> Show one or two target attachments in your hand. Shuffle them into your Fate deck. Draw cards equal to the number you showed plus one."
Conservation = Strategy(card_id=12226, title='Conservation', focus_value=4, keywords=[Courage], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Interrupt:</b> Bow your target unbowed Weapon to negate the action's Melee and Ranged Attacks. <br><b>Battle:</b> Give your target opposed Kensai with a Weapon +2F."
Defensive_Technique = Strategy(card_id=12227, title='Defensive Technique', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Open:</b> Put this Kata into play. Discard your other Kata in play.<br><b>Interrupt, :bow::</b> If the action is another player's, put your attachments in your hand instead of in your discard pile when the action destroys them or their Personality."
Diligent_Care = Strategy(card_id=12228, title='Diligent Care', focus_value=2, keywords=[Kharmic, Kata], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Absent Battle:</b> If he would be opposed, move your target Tactician at home to the current battlefield. <i>(Absent actions may be taken without presence.)</i><br><b>Battle, :g3::</b> Put a Battle Strategy in your discard pile into your hand.'
Feinting_Maneuver = Strategy(card_id=12229, title='Feinting Maneuver', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Absent Battle:</b> If he would be opposed, move your target Personality at home to the current battlefield. If he is a Duelist, straighten him as he moves. <i>(Absent actions may be taken without presence.)</i>'
Gaining_an_Edge = Strategy(card_id=12230, title='Gaining an Edge', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Invest :g1::</b> If your Personality is a Duelist, draw a card.<br><b>Interrupt:</b> After the action starts a duel, if your Personality in it has a lower duel stat than the other <i>(at that time)</i>, then each player must focus at least once in the duel, and give the first card you focused in the duel +2FV after it is revealed.'
Hidden_Strength = Strategy(card_id=12231, title='Hidden Strength', focus_value=4, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Absent Interrupt:</b> Negate the action if it is Engage.<br><b>Battle:</b> Move home your target Personality. Straighten his unit as he moves.'
Lookout_Post = Strategy(card_id=12233, title='Lookout Post', focus_value=4, keywords=[Kharmic], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Open:</b> Put this Kata into play. Discard your other Kata in play.<br><b>Absent Battle, :bow::</b> If the current enemy army has any units, transfer your target Fortification at its battlefield to another Province.'
Mastery_of_Chikujo = Strategy(card_id=12234, title='Mastery of Chikujo', focus_value=3, keywords=[Kharmic, Kata], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Straighten one or two target Followers.<br><b>Open:</b> Put your target discarded <i>(not dead)</i> Commander into one of your Provinces, discarding any other cards there.'
Powerful_Motivation = Strategy(card_id=12235, title='Powerful Motivation', focus_value=2, keywords=[Courage], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Battle:</b> Fear 2.<br><b>Battle:</b> Fear equal to your target unbowed Magistrate's Chi plus Personal Honor that must target a dishonorable or Shadowlands Personality, who may have <b>Followers</b>."
Public_Arrest = Strategy(card_id=12236, title='Public Arrest', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Fear 3 <i>(Bow a target enemy Follower or Personality without Followers with 3 or lower Force)</i>.<br><b>Battle:</b> Bow one to four target enemy Personalities, each with 4 or lower Gold Cost and with a total combined Gold Cost of 8 or less.'
Scour_the_Unworthy = Strategy(card_id=12237, title='Scour the Unworthy', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Ninja Battle:</b> Give a target enemy Personality a -1F/-1C <b>Poison </b>token. Straighten your Sensei; you may use its abilities again this turn. You may target and bow your unbowed Ninja to give the Personality an additional -1F/-1C Poison token after each time your Ninja action resolves that targeted him, not including this one. Lose 2 Honor.'
Spinning_the_Web = Strategy(card_id=12238, title='Spinning the Web', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy Personality -2F. <br><b>Battle:</b> Give a target enemy Personality with 6 or more Force -4F. You may take an additional action.'
Startling_Kiai = Strategy(card_id=12239, title='Startling Kiai', focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Battle:</b> Give a target enemy Follower or Personality a Force penalty equal to your target unbowed Follower's Force. If that Follower is attached to a Commander, you may bow it to draw a card and take an additional action."
Superior_Defense = Strategy(card_id=12240, title='Superior Defense', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Political Open:</b> Target a Human Personality. He must undergo a test of character. Discard the top card of his controller's Fate Deck. If the Focus Value is greater than or equal to the target's Personal Honor, dishonor him and draw a card."
Test_of_Character = Strategy(card_id=12241, title='Test of Character', focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Earth Open:</b> If you don't have a Ring in play, target three Personalities controlled by the active player. He must declare an attack this turn and assign at least one of them, if able.<br><b>Earth Open:</b> Give your Provinces +2 strength for each Ring you control <i>(this turn)</i>."
Walking_with_the_Earth = Strategy(card_id=12242, title='Walking with the Earth', focus_value=4, keywords=[Courage], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle/Open:</b> Straighten your target Ring.<br><b>Fire Interrupt:</b> Bow your target unbowed Ring. After revealing focused cards in a duel created by the action, give the first card you focused in the duel +2FV.'
Walking_with_the_Fire = Strategy(card_id=12243, title='Walking with the Fire', focus_value=2, keywords=[Kharmic], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Political Open:</b> Give another player's target Personality -2F. You may target and bow your unbowed Magistrate to dishonor the Personality."
Warranted_Search = Strategy(card_id=12244, title='Warranted Search', focus_value=2, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])