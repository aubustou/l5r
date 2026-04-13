from __future__ import annotations
from .common import Strategy
from l5r_auto.keywords import Economic, Favor, Iaijutsu, Kata, Kharmic, Kiho, Political, Terrain
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Invest :g1:: For each target with 0 Personal Honor, his controller loses 1 Honor. <i>(After this card is played, you may also pay the Invest cost to get the effect, once.)</i><br><b>Political Open:</b> Target two Personalities controlled by the same player. They may not attack in the same army <i>(this turn)</i>.'
A_Growing_Rift = Strategy(card_id=11821, title='A Growing Rift', focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Favor Political Battle, :g3::</b> If he would be opposed, discard the Imperial Favor to create a 5F/5C/3PH Imperial &#149; Ivory Champion &#149; Magistrate &#149; Samurai &#149; <b>Cavalry</b> Personality. Remove him from the game after the battle ends.'
Arrival_of_the_Ivory_Champion = Strategy(card_id=11822, title='Arrival of the Ivory Champion', focus_value=4, keywords=[Favor, Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Bow your target unbowed Personality. Fear equal to his Force. If he is a Kensai, you may bow one of his Weapons to straighten him.'
Bitter_Lies_Technique = Strategy(card_id=11823, title='Bitter Lies Technique', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Your Followers at this battlefield have +1F.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Bleak_Lands = Strategy(card_id=11824, title='Bleak Lands', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Bow your target unbowed Courtier or Shugenja at any location. Target your Personality. Give him +2F if he is opposed. Straighten him if he is a Yojimbo.'
Bonds_of_Service = Strategy(card_id=11825, title='Bonds of Service', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Political Open:</b> Bow your two target unbowed Personalities, and give each of them who is not a Courtier -1C while this action resolves. Bow a target Personality whose unit's Force is lower than the two Personalities' total Chi. Lose 2 Honor."
Contained_at_Court = Strategy(card_id=11826, title='Contained at Court', focus_value=3, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Absent Battle:</b> If he would be opposed, move your target unbowed Personality at home to the current battlefield. If he is a Kensai, you may take an additional action to use an ability on one of his Weapons. <i>(Absent actions may be taken without presence.)</i>'
Death_from_Above = Strategy(card_id=11827, title='Death from Above', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Your defending Personalities have +1F, and +1F for each of their attachments.<br><b>Battle:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Defending_the_City = Strategy(card_id=11828, title='Defending the City', focus_value=2, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"As a Focus Effect, if the Challenger is Fallen or his duel stat was higher than his opponent's by 3 or more when the duel began, destroy both participants and end the duel without resolution.<br><b>Battle, :g1::</b> Move home a target attacking Personality."
Deny_the_False_Form = Strategy(card_id=11829, title='Deny the False Form', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Destroy a target Terrain and bow a target enemy Personality. If you are a Phoenix Clan player and the Terrain is yours, put it into your hand.'
Discovering_the_Anvil_of_Earth = Strategy(card_id=11830, title='Discovering the Anvil of Earth', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Straighten your target Personality. If he has 3 or more Personal Honor, or is Lion Clan, you may take an additional action to use an ability printed on the Personality.'
Discovering_the_Daisho_of_Water = Strategy(card_id=11831, title='Discovering the Daisho of Water', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This ability's Gold cost is 2 if you are a Crab Clan player or control a Tactician.<br><b>Battle/Open, :g3::</b> Target three Fate cards in your discard pile with different titles. Another player chooses one of them; remove it from the game. Put one of the remaining two cards into your hand."
Discovering_the_Seeds_of_the_Void = Strategy(card_id=11832, title='Discovering the Seeds of the Void', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This card's ability is <b>Battle/Open</b> if you are a Unicorn Clan player.<br>Invest :g2:: Straighten a target Courtier. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br><b>Open:</b> Straighten a target Personality."
Discovering_the_Shakuhachi_of_Air = Strategy(card_id=11833, title='Discovering the Shakuhachi of Air', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Invest :g2:, or :g0: if the first target is a Tactician: Take an additional action <i>(after this one resolves)</i>.<br><b>Battle:</b> Target your Personality and another Personality. Give your Personality +1F and he copies an ability on the second target which does not copy abilities.'
Inspired_Leadership = Strategy(card_id=11834, title='Inspired Leadership', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Interrupt:</b> Bow your target unbowed Follower or Personality. Give a Fear effect, Melee Attack, or Ranged Attack -2 strength, or -3 strength if this action bowed a Yojimbo or Crab Clan Personality.'
Iron_and_Stone = Strategy(card_id=11835, title='Iron and Stone', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Kiho Battle:</b> Target your unbowed Monk or Shugenja. Fear equal to his Chi <i>(Bow a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Fear's strength)</i>."
Kharmic_Threat = Strategy(card_id=11836, title='Kharmic Threat', focus_value=3, keywords=[Kharmic, Kiho], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(<b>Repeatable Limited,</b> :g2:: Discard a Kharmic card to draw a card.)</i><br><b>Political Open:</b> The player with the Imperial Favor discards it and loses 2 Honor.'
Losing_Favor = Strategy(card_id=11837, title='Losing Favor', focus_value=4, keywords=[Kharmic, Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Battle:</b> Bow your target unbowed Follower. Melee Attack equal to its Force <i>(Destroy a target enemy Follower, or Personality without Followers, with Force equal to or lower than the Melee Attack's strength)</i>."
Merciless_Assault = Strategy(card_id=11838, title='Merciless Assault', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After your Personality moves to, or enters play at, this battlefield, give him +1F.<br><b>Battle/Engage:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play.'
Open_Roads = Strategy(card_id=11839, title='Open Roads', focus_value=2, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Economic Battle, :gstar::</b> Move home a target Personality with Chi less than or equal to the amount paid. Lose 1 Honor.'
Persuasive_Tactics = Strategy(card_id=11840, title='Persuasive Tactics', focus_value=2, keywords=[Economic], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :gstar::</b> Equip a target attachment from your hand <i>(Followers, Items, and Spells are attachments)</i>. Take an additional action.'
Proper_Equipment = Strategy(card_id=11841, title='Proper Equipment', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Target your unbowed Personality. Bow a target enemy card with less Force and without attachments.'
Punishing_Blow = Strategy(card_id=11842, title='Punishing Blow', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'As a Focus Effect, if the duel is not during a battle, end the duel without resolution. <i>(Other Focus Effects resolve.)</i><br><b>Battle:</b> Straighten your target opposed card. Give a target Follower or Personality +1F or -1F.'
Relentless = Strategy(card_id=11843, title='Relentless', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Political Battle:</b> Bow your target unbowed Courtier. Each other player targets a Personality he controls <i>(if able)</i>. Move home all targets. A target player gains or loses 1 Honor.'
Relocating_the_Court = Strategy(card_id=11844, title='Relocating the Court', focus_value=1, keywords=[Political], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Interrupt:</b> Negate an Engage action from a Strategy.<br><b>Battle:</b> Give your target opposed Scout +2F.'
Scout_Training = Strategy(card_id=11845, title='Scout Training', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Invest :g1:: Draw a card if the Personality is a Scout. <i>(After this card is played, you may also pay the Invest cost to get the effect, once.)</i><br><b>Absent Interrupt:</b> After your action resolves, if it Recruited your Personality during a battle, take an additional action.'
Signal_the_Scouts = Strategy(card_id=11846, title='Signal the Scouts', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After this Strategy enters your discard pile, give a target Personality -2F.<br><b>Battle:</b> Give your target opposed Personality +2F.'
Strength_in_Subtlety = Strategy(card_id=11847, title='Strength in Subtlety', focus_value=1, keywords=[Kharmic], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Engage:</b> Give a target enemy Personality -2F.<br><b>Battle:</b> Give a target enemy Personality -2F/-1C.'
Strike_as_the_Earth = Strategy(card_id=11848, title='Strike as the Earth', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Engage:</b> Give your target opposed Personality +2F/+1C.<br><b>Battle:</b> Give your target opposed Personality +2F/+1C/+1PH.'
Strike_as_the_Wind = Strategy(card_id=11849, title='Strike as the Wind', focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After a Personality moves to this battlefield, his controller must target and bow an unbowed card in his unit.<br><b>Absent Battle/Engage:</b> Destroy a Terrain <i>(if able)</i>. Put this Terrain into play. <i>(Absent actions may be taken without presence.)</i>'
Sudden_Storm = Strategy(card_id=11850, title='Sudden Storm', focus_value=1, keywords=[Terrain], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'As a Focus Effect, the winner gains 2 Honor.<br><b>Engage:</b> Give your target defending Personality +2F. If he is a Duelist, the next time this battle he is in a duel, the other player must focus at least once <i>(if able)</i>.'
Swan_Technique = Strategy(card_id=11851, title='Swan Technique', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>Battle:</b> Target your Personality. Give a target enemy Follower or Personality a Force penalty equal to your Personality's Chi plus Personal Honor. Destroy your Personality."
Taken_Hostage = Strategy(card_id=11852, title='Taken Hostage', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Iaijutsu Battle:</b> Your target unbowed Personality challenges a target enemy Personality. Bow the loser. Destroy him if the last Battle action his owner took this battle destroyed one of your Personalities.'
The_Eternal_Chase = Strategy(card_id=11853, title='The Eternal Chase', focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After the first time each turn any of your Personalities wins a duel, give him a +1F token. After your first challenge each turn is refused, gain 1 Honor.<br><b>Open:</b> Put this Kata into play. Discard all your other Kata in play.'
Thousand_Year_Rivalry = Strategy(card_id=11854, title='Thousand Year Rivalry', focus_value=3, keywords=[Kharmic, Kata], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy Personality -2F. If he has a Poison token, give him a -1F/-1C <b>Poison</b> token.'
Unsanctioned_Strike = Strategy(card_id=11855, title='Unsanctioned Strike', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Crab Clan player, this Strategy has Discipline :g1:. <br><b>Battle:</b> Straighten your target Personality. Negate all Force penalties on him. He has +2F while his army is opposed. Destroy him before the turn ends.'
Way_of_the_Crab = Strategy(card_id=11856, title='Way of the Crab', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Crane Clan player, this Strategy has Discipline :g3:. <br><b>Iaijutsu Battle:</b> Your target unbowed Personality challenges a target enemy Personality, whose controller can dishonor him and move him home to refuse. Bow the loser. The winner gains 1 Honor.'
Way_of_the_Crane = Strategy(card_id=11857, title='Way of the Crane', focus_value=4, keywords=[Iaijutsu], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Dragon Clan player, this Strategy has Discipline :g2:.<br><b>Iaijutsu Battle:</b> Your target unbowed Personality challenges a target enemy Personality. Give the winner +2F. Give the loser -2F, and bow him if he is dishonorable.'
Way_of_the_Dragon = Strategy(card_id=11858, title='Way of the Dragon', focus_value=4, keywords=[Iaijutsu], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Lion Clan player, this Strategy has Discipline :g2:. <br><b>Battle:</b> Target your unbowed Personality. Fear equal to his Personal Honor that destroys Followers after it bows them.'
Way_of_the_Lion = Strategy(card_id=11859, title='Way of the Lion', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Mantis Clan player, this Strategy has Discipline :g3:.<br><b>Battle:</b> Straighten your target Personality. You may use his abilities with Ranged Attack effects an additional time this turn.'
Way_of_the_Mantis = Strategy(card_id=11860, title='Way of the Mantis', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Phoenix Clan player, this Strategy has Discipline :g1:.<br><b>Battle:</b> Straighten your target Spell. You may use its abilities an additional time this turn. Take an additional action.'
Way_of_the_Phoenix = Strategy(card_id=11861, title='Way of the Phoenix', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Scorpion Clan player, this Strategy has Discipline :g2:.<br><b>Open, :g1::</b> Target a Personality whose Personal Honor is less than printed. His controller loses Honor equal to the difference. Look at two cards in his hand or Provinces.'
Way_of_the_Scorpion = Strategy(card_id=11862, title='Way of the Scorpion', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Spider Clan player, this Strategy has Discipline :g3:. <br><b>Battle:</b> Fear 2.<br><b>Interrupt:</b> Give a Fear effect +2 strength. Destroy any Follower after it bows them.'
Way_of_the_Spider = Strategy(card_id=11863, title='Way of the Spider', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'If you are a Unicorn Clan player, this Strategy has Discipline :g3:. <br><b>Battle:</b> Target your Personality, who may be at home. Move him home or, if his unit is Cavalry and he would be opposed, move him to the current battlefield.'
Way_of_the_Unicorn = Strategy(card_id=11864, title='Way of the Unicorn', focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])