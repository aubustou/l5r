from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, BattleMaiden, Cat, Cavalry, Conscript, Courage, Earth, Experienced, Honor, Mercenary, Monk, Ninja, Nonhuman, Oni, Pirate, Ronin, Scout, Shadowlands, Shugenja, Spirit
from l5r_auto.legality import ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Battle:</b> Give one or two target enemy Personalities, each with a different Clan Alignment, -2F each.'
Brotherhood_Sohei = Follower(card_id=12499, title='Brotherhood Sohei', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Monk], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Follower enters play from your hand, draw an additional card before your turn ends.'
Courageous_Ashigaru = Follower(card_id=12500, title='Courageous Ashigaru', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Ashigaru, Conscript], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"<b>Interrupt:</b> Negate the action's challenges to this Personality if the challenger has no Followers.<br><b>Battle, :bow::</b> Ranged 3 Attack."
Defensive_Archers = Follower(card_id=12501, title='Defensive Archers', force=3, chi=0, gold_cost=5, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"Reduce the Gold cost to Equip this Follower by the Personality's Personal Honor.<br><b>Interrupt:</b> Negate this Personality's movement from the action."
Emerald_Guard = Follower(card_id=12502, title='Emerald Guard', force=4, chi=0, gold_cost=9, focus_value=4, keywords=[Honor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'This Follower has +1F for each bowed Follower and bowed Personality opposing it.<br>After you discard this Follower from your hand for a Courage Interrupt, you may take an additional action to Equip it <i>(after the original action resolves)</i>.'
Legendary_Warcat = Follower(card_id=12503, title='Legendary Warcat', force=3, chi=0, gold_cost=5, focus_value=1, keywords=[Courage, Cat, Nonhuman], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"After this Follower enters play, lose 2 Honor.<br><b>Ninja Open:</b> Look at a face-down card in another player's Province."
Master_Infiltrator = Follower(card_id=12504, title='Master Infiltrator', force=1, chi=0, gold_cost=0, focus_value=3, keywords=[Ninja, Scout], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Follower enters play, lose 4 Honor.<br><b>Battle:</b> Fear 2 that destroys Followers after it bows them.'
Oni_Familiar = Follower(card_id=12505, title='Oni Familiar', force=3, chi=0, gold_cost=3, focus_value=2, keywords=[Cavalry, Nonhuman, Oni, Shadowlands], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'After this Follower enters play, lose 1 Honor.<br><b>Ninja Battle, :g2::</b> Ranged 3 Attack <i>(Destroy a target enemy Follower or Personality without Followers with 3 or lower Force)</i>.'
Questionable_Vassal = Follower(card_id=12506, title='Questionable Vassal', force=2, chi=0, gold_cost=2, focus_value=3, keywords=[Mercenary, Ninja, Ronin], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"After this Follower enters play, gain 1 Honor. This Personality has +1PH. After this unit moves to oppose a defender, gain 1 Honor.<br><b>Battle, :bow::</b> Fear equal to this Personality's Personal Honor."
Shiotome_Troupe = Follower(card_id=12507, title='Shiotome Troupe', force=2, chi=0, gold_cost=4, focus_value=2, keywords=[Cavalry, BattleMaiden, Honor], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Repeatable Interrupt: Discard a Courage card to give a Fear effect +2 or -2 strength.)</i><br><b>Battle, :g2::</b> Give another target opposed Mercenary +2F.'
Sons_of_Gusai_Experienced = Follower(card_id=12508, title='Sons of Gusai', force=2, chi=0, gold_cost=2, focus_value=2, keywords=[Courage, Experienced('1'), Mercenary, Pirate], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'<i>(Repeatable Interrupt: Discard an Honor card to give an Honor gain or loss +1 or -1.)</i><br><b>Absent Home Battle:</b> Move this Personality to the current battlefield if any enemy attacking units are there. Straighten the Personality as he or she moves.'
Spiritual_Sentries = Follower(card_id=12509, title='Spiritual Sentries', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Honor, Nonhuman, Spirit], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
"After this Personality straightens, straighten this Follower. <br><b>Earth Battle, :bow::</b> Fear equal to twice this Follower's Force."
The_Mountainborn_Experienced = Follower(card_id=12510, title='The Mountainborn', force=3, chi=0, gold_cost=6, focus_value=1, keywords=[Experienced('Bound Spirit'), Earth, Nonhuman, Shugenja, Spirit], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])
'Negate Fear effects targeting this Follower while it is opposing a bowed Follower or Personality.<br><b>Battle:</b> Fear 2 or give a target enemy Follower or Personality -2F.'
WarcatsinTraining = Follower(card_id=12511, title='Warcats-in-Training', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Cavalry, Cat, Nonhuman], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, ModernEdition])