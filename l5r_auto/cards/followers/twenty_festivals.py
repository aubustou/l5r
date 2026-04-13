from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cat, Cavalry, Expendable, Mercenary, Nonhuman, Ronin, Shadowlands, Shugenja, Undead
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle, :bow::</b> Melee 3 Attack.<br><b>Tireless Battle, :g3::</b> Straighten this Follower.'
Amoral_Wave_Men = Follower(card_id=12193, title='Amoral Wave Men', force=3, chi=0, gold_cost=6, focus_value=1, keywords=[Mercenary, Ronin], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Heavy_Cavalry = Follower(card_id=12194, title='Fearless Heavy Cavalry', force=4, chi=0, gold_cost=7, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Heavy_Infantry = Follower(card_id=12195, title='Fearless Heavy Infantry', force=5, chi=0, gold_cost=9, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Light_Cavalry = Follower(card_id=12196, title='Fearless Light Cavalry', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Light_Infantry = Follower(card_id=12197, title='Fearless Light Infantry', force=2, chi=0, gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Medium_Cavalry = Follower(card_id=12198, title='Fearless Medium Cavalry', force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower.<br><b>Interrupt:</b> If the action is yours, straighten this Follower after it resolves.'
Fearless_Medium_Infantry = Follower(card_id=12199, title='Fearless Medium Infantry', force=3, chi=0, gold_cost=4, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After a battle resolution in which this Follower was in an army that destroyed any enemy units or a Province, gain 2 Honor.'
Personal_Instructor = Follower(card_id=12200, title='Personal Instructor', force=2, chi=0, gold_cost=2, focus_value=3, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'This Personality, if he is a Shugenja, has +1C while actions on your Kihos and Spells are resolving.'
Shugenja_Aide = Follower(card_id=12201, title='Shugenja Aide', force=3, chi=0, gold_cost=3, focus_value=1, keywords=[Shugenja], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Follower enters play, lose 4 Honor.<br><b>Battle:</b> Ranged 3 Attack.'
The_Unquiet_Moto = Follower(card_id=12202, title='The Unquiet Moto', force=3, chi=0, gold_cost=5, focus_value=0, keywords=[Cavalry, Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Draw a card after your Expendable card dies.)</i>'
Young_Battlecat = Follower(card_id=12203, title='Young Battlecat', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Expendable, Cat, Nonhuman], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Interrupt:</b> After this Follower enters play, search your discard pile, then deck, for a Young Battlecat, show it, and put it in your hand.<br><b>Battle, :bow::</b> Melee 2 Attack, with +1 strength if the target is an Infantry Follower.'
Zaiko = Follower(card_id=12204, title='Zaiko', force=3, chi=0, gold_cost=6, focus_value=1, keywords=[Cavalry, Cat, Nonhuman], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])