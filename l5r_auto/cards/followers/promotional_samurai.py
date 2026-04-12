from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Jade, Monk, Scout, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, SamuraiEdition, TwentyFestivalsEdition
'<b>Open:</b> Create a 3F/1C/1PH Scout &#149; <b>Cavalry</b> Personality. Remove this Follower from the game.'
Baraunghar_Scouts = Follower(card_id=699, title='Baraunghar Scouts', force=3, chi=0, gold_cost=5, focus_value=2, keywords=[Cavalry, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Straighten a target Daimyo, Duelist, or Kensai Personality.'
Brothers_of_Jade = Follower(card_id=1168, title='Brothers of Jade', force=3, chi=0, gold_cost=4, focus_value=3, keywords=[Jade, Monk], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, SamuraiEdition, ModernEdition])
'<b>Battle, :g*::</b> If this Follower is in your hand, target your Personality at any location. If he would be opposed, move him to the current battlefield and Equip this Follower to him.'
Hidden_Reserves = Follower(card_id=3261, title='Hidden Reserves', force=2, chi=0, gold_cost=3, focus_value=1, keywords=[Scout], traits=[], abilities=[], legality=[TwentyFestivalsEdition, OnyxEdition, SamuraiEdition, ModernEdition])
'<b>Battle, :bow::</b> Draw a card.'
Hired_Legion = Follower(card_id=3277, title='Hired Legion', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=0, keywords=[Unique], traits=[], abilities=[], legality=[EmperorEdition, SamuraiEdition, ModernEdition])