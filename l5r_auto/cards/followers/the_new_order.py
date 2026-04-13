from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Earth, Mercenary, Monk, Nonhuman, Ratling, Reserve, Ronin, Shadowlands, Shugenja, Spirit, Undead
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'While you control one or more Rings, this Follower has <b>Expendable</b>. While you control two or more Rings, this Personality has <b>Cavalry</b>. While you control three or more Rings, this Follower has +1F.'
Anonymous_Monk = Follower(card_id=11947, title='Anonymous Monk', force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Cavalry, Monk], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Followers cannot attach Spells.)</i><br><b>Unstoppable Battle:</b> Fear 2, or Fear 3 if this Follower is attached to an Earth Shugenja. <i>(Other players cannot Interrupt Unstoppable actions.)</i>'
Bound_Spirit = Follower(card_id=11953, title='Bound Spirit', force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Earth, Nonhuman, Shugenja, Spirit], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Melee 2 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 2 or lower Force)</i>.'
Boyoh_Spearmen = Follower(card_id=11944, title='Boyoh Spearmen', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Mercenary, Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Fear effects, Melee Attacks, and Ranged Attacks targeting this Follower have -2 strength.'
Gifted_Officer = Follower(card_id=11954, title='Gifted Officer', force=4, chi=0, gold_cost=7, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
Hachiros_Legion = Follower(card_id=11946, title="Hachiro's Legion", force=4, chi=0, gold_cost=5, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i> <br><b>Unstoppable Battle:</b> Fear equal to this Personality's Personal Honor. <i>(Other players cannot Interrupt Unstoppable actions.)</i>"
Jovial_Ronin = Follower(card_id=11950, title='Jovial Ronin', force=2, chi=0, gold_cost=4, focus_value=3, keywords=[Cavalry, Mercenary, Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> Fear 2. If this fails to bow a card because the card is already bowed, destroy that card.'
Nezumi_Remnants = Follower(card_id=11949, title='Nezumi Remnants', force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Cavalry, Nonhuman, Ratling], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle, :bow::</b> Ranged 2 Attack. Straighten this Follower if this unit moved this turn.'
Shinjo_Archers = Follower(card_id=11945, title='Shinjo Archers', force=3, chi=0, gold_cost=6, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Fear effects, Melee Attacks, and Ranged Attacks targeting this Follower have -1 strength. <br><b>Battle:</b> Ranged 3 Attack.'
Trained_Horsemen = Follower(card_id=11951, title='Trained Horsemen', force=5, chi=0, gold_cost=12, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Fear effects, Melee Attacks, and Ranged Attacks targeting this Follower have -1 strength. <br><b>Battle:</b> Melee 3 Attack.'
Trained_Swordsmen = Follower(card_id=11952, title='Trained Swordsmen', force=5, chi=0, gold_cost=11, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"After you Equip this Follower, lose 3 Honor. <br>After the first time each battle a Personality or Follower is destroyed at this card's battlefield, create a 1F <b>Nonhuman &#149; Shadowlands &#149; Undead</b> Follower and attach it to this Personality.<br><b>Battle:</b> Fear equal to the number of Undead cards in this unit."
Unliving_Legion = Follower(card_id=11955, title='Unliving Legion', force=3, chi=0, gold_cost=3, focus_value=1, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<i>(You may Equip a Reserve attachment, if it would be opposed, as a <b>Battle</b> action.)</i> <br>After this Follower is destroyed by another player's action or by battle resolution, put it in your hand."
Victorious_Wave_Men = Follower(card_id=11948, title='Victorious Wave Men', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Reserve, Mercenary, Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])