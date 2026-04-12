from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Nonhuman, Scout, Shadowlands, Undead
from l5r_auto.legality import GoldEdition, ImperialEdition, IvoryEdition, JadeEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i>'
Light_Cavalry = Follower(card_id=4733, title='Light Cavalry', force=2, chi=0, gold_cost=2, focus_value=1, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
'<i>(Once per turn, as an Absent Engage, move your unbowed Personality in a Cavalry unit to this battle.)</i>'
Medium_Cavalry = Follower(card_id=5016, title='Medium Cavalry', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Cavalry], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
Medium_Infantry = Follower(card_id=5017, title='Medium Infantry', force=3, chi=0, gold_cost=3, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, ModernEdition])
'<b>Engage:</b> Take an additional Battle action to play a Terrain.'
Scout = Follower(card_id=6505, title='Scout', force=0, chi=0, gold_cost=1, focus_value=2, keywords=[Cavalry, Scout], traits=[], abilities=[], legality=[ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, TwentyFestivalsEdition])
'Ranged Attacks cannot target cards in this unit.'
Shield_Wall = Follower(card_id=6840, title='Shield Wall', force=0, chi=0, gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ImperialEdition, GoldEdition, JadeEdition, ModernEdition])
'After you Equip this Follower, lose 4 Honor.<br><b>Battle:</b> Fear 3.'
Zombie_Troops = Follower(card_id=9709, title='Zombie Troops', force=3, chi=0, gold_cost=3, focus_value=1, keywords=[Nonhuman, Shadowlands, Undead], traits=[], abilities=[], legality=[ImperialEdition, GoldEdition, JadeEdition, OnyxEdition, TwentyFestivalsEdition])