from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, BattleMaiden, Cat, Cavalry, Conscript, Earth, Expendable, Nonhuman, Shadowlands, Spirit, Undead
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(Draw a card after your Expendable card dies.)</i><br>This Personality cannot attack. After this Follower is destroyed, gain 2 Honor.'
Caravan_Guards = Follower(card_id=12343, title='Caravan Guards', force=2, chi=0, gold_cost=4, focus_value=4, keywords=[Expendable], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Open, :bow::</b> Create a 1F <b>Ashigaru </b> and attach it to your target Personality.'
Conscription_Officer = Follower(card_id=12344, title='Conscription Officer', force=1, chi=0, gold_cost=5, focus_value=2, keywords=[Ashigaru], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'This Follower has +1F for each other Ashigaru in this unit.'
Fresh_Recruits = Follower(card_id=12345, title='Fresh Recruits', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Ashigaru], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Earth Battle, :bow::</b> Melee 3 Attack. Straighten this Follower if it is attached to an Earth Personality.'
Hirakuras_Attendant = Follower(card_id=12346, title="Hirakura's Attendant", force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Earth, Nonhuman, Spirit], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Engage:</b> Give a target Follower or Personality +2F or -2F.<br><b>Battle, :bow::</b> Ranged 3 Attack.'
Junghar_Regulars = Follower(card_id=12347, title='Junghar Regulars', force=2, chi=0, gold_cost=7, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Follower enters play, lose 2 Honor. <br><b>Interrupt:</b> If the action is from an Undead card, its Fear effects may target Items and Spells, and destroy attachments after they bow them.'
Legion_of_the_Ninth_Kami = Follower(card_id=12348, title='Legion of the Ninth Kami', force=3, chi=0, gold_cost=3, focus_value=2, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"Compassion: This Follower's printed ability has no bow cost. <i>(Compassion takes effect while you have fewer Provinces than anyone else.)</i><br><b>Battle, :bow::</b> Melee 3 Attack."
Razorfang = Follower(card_id=12349, title='Razorfang', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Cat, Nonhuman], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy defending Personality -3F. Gain 1 Honor if his Force is now 0.'
Shiotome_Patrol = Follower(card_id=12350, title='Shiotome Patrol', force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Cavalry, BattleMaiden], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Fear 3 that, if this unit is Cavalry, destroys Infantry cards after it bows them <i>(Bow a target enemy Follower or Personality without Followers with 3 or lower Force)</i>.'
The_Thundering_Death = Follower(card_id=12351, title='The Thundering Death', force=4, chi=0, gold_cost=8, focus_value=1, keywords=[Cavalry], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<b>Battle:</b> Straighten your target Ashigaru.'
Village_Defenders = Follower(card_id=12352, title='Village Defenders', force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Ashigaru, Conscript], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])