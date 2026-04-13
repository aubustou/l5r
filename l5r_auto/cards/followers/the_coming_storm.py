from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Expendable, Experienced, Guard, Merchant, Nonhuman, Reserve, Ronin, Scout, Zokujin
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<i>(You may Equip a Reserve attachment, if it would be opposed, as a <b>Battle</b> action.)</i><br><b>Interrupt:</b> After the action Equips this Follower at a battlefield, Fear 3.'
Assault_Unit = Follower(card_id=11787, title='Assault Unit', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Reserve], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Can only attach to a Samurai. <br><b>Engage, :bow::</b> Create and attach a +2F/+0C Armor Item to this Personality. Remove it from the game after this battle ends.'
Battle_Attendants = Follower(card_id=11788, title='Battle Attendants', force=2, chi=0, gold_cost=4, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Draw a card after your Expendable card dies.)</i><br>This Personality cannot attack.'
Defensive_Miko = Follower(card_id=11790, title='Defensive Miko', force=3, chi=0, gold_cost=2, focus_value=4, keywords=[Expendable], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Invest :g3:: Give this Follower two +1F tokens.<i>(After this card enters play, you may also pay the Invest cost to get the effects, once.)</i><br>After this unit moves, give this Follower +1F.'
Mobile_Troops = Follower(card_id=11791, title='Mobile Troops', force=0, chi=0, gold_cost=1, focus_value=3, keywords=[Cavalry, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This Follower has a Force bonus equal to this Personality's Personal Honor."
Personal_Guard = Follower(card_id=11792, title='Personal Guard', force=1, chi=0, gold_cost=5, focus_value=4, keywords=[Guard], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"<b>:bow::</b> Produce 2 Gold, which may only pay for one Economic action's cost."
Profiteer = Follower(card_id=11793, title='Profiteer', force=1, chi=0, gold_cost=2, focus_value=2, keywords=[Merchant], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to the battle.)</i><br><b>Battle:</b> Discard a card to make a Fear effect with strength equal to its Focus Value.'
Samurai_Lancers = Follower(card_id=11794, title='Samurai Lancers', force=2, chi=0, gold_cost=3, focus_value=3, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Tireless Battle:</b> Transfer this Follower to another of your target Personalities. After it transfers, straighten it. <i>(Tireless actions may be taken even while bowed.)</i>'
Traveling_Ronin_Experienced = Follower(card_id=11795, title='Traveling Ronin', force=3, chi=0, gold_cost=4, focus_value=1, keywords=[Experienced('1'), Ronin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Repeatable Battle, :bow::</b> Ranged 3 Attack. <i>(Repeatable actions may be taken any number of times per turn.)</i>'
Yomanri_Archers = Follower(card_id=11796, title='Yomanri Archers', force=2, chi=0, gold_cost=6, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Battle:</b> If this Follower is attacking, Fear 4 that may target a Personality with Followers. <i>(Bow a target enemy Follower or Personality with 4 or lower Force.)</i>'
Zlkyts_Family = Follower(card_id=11797, title="Zlkyt's Family", force=2, chi=0, gold_cost=3, focus_value=2, keywords=[Nonhuman, Zokujin], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])