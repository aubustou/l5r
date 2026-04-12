from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Bandit, Cavalry, Guard, Ninja, Shadowlands, Thunder
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'This Follower has +1F for every two Farms you control.'
Ashigaru_Guards = Follower(card_id=615, title='Ashigaru Guards', force=0, chi=0, personal_honor=0, gold_cost=0, focus_value=1, honor_requirement=0, keywords=[Ashigaru], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Transfer this Follower to your target Personality.'
Field_Messenger = Follower(card_id=2520, title='Field Messenger', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=3, honor_requirement=0, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect, you may transfer a Follower from your Personality in this duel to another of your Personalities.<br><b>Battle:</b> Move a target Personality at the current battlefield home or to an adjacent battlefield.'
Flanking_Unit = Follower(card_id=2598, title='Flanking Unit', force=4, chi=0, personal_honor=0, gold_cost=7, focus_value=1, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, you may attach this card to one of your Personalities, ignoring Gold cost.<br><b>Battle:</b> Bow this card: Ranged 6 Attack.'
Hiromis_Vassals = Follower(card_id=3280, title="Hiromi's Vassals", force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=0, keywords=[Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'As a Focus Effect: After this duel ends, give your Personality in it +3F.<br>This card has +3F while defending.<br><b>Battle:</b> Target an enemy card without attachments: Bow it. Gain 2 Honor.'
Home_Guard = Follower(card_id=3413, title='Home Guard', force=1, chi=0, personal_honor=0, gold_cost=2, focus_value=4, honor_requirement=3, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow this card: Melee 3 Attack.'
Murderous_Thieves = Follower(card_id=5445, title='Murderous Thieves', force=0, chi=0, personal_honor=0, gold_cost=0, focus_value=3, honor_requirement=0, keywords=[Bandit], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Will only attach to a Ninja.<br>This Follower has <b>a</b> Force bonus equal to its Personality's printed Force."
Ninja_Guards = Follower(card_id=5565, title='Ninja Guards', force=0, chi=0, gold_cost=4, focus_value=1, honor_requirement=0, keywords=[Guard, Ninja], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'After this card enters play: Lose 1 Honor.<br>This Personality has Conqueror.<br><b>Battle:</b> Melee 4 Attack.'
Village_Raiders = Follower(card_id=9163, title='Village Raiders', force=4, chi=0, personal_honor=0, gold_cost=6, focus_value=2, honor_requirement=0, keywords=[Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])