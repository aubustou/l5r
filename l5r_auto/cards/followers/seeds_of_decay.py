from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Cavalry, Ninja, Ronin, Scout
from l5r_auto.legality import EmperorEdition, ModernEdition
"<b>Reaction:</b> After another player's action targets this Personality, remove this card from the game to create a 3F/1C/2PH <b>Samurai &#149; Cavalry</b> Personality with your Clan Alignment at the target's location. Transfer the target's attachments to the created Personality."
Cavalry_Detachment = Follower(card_id=10105, title='Cavalry Detachment', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=0, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Melee 4 Attack, or Melee 5 Attack if the target is Infantry.'
Horseback_Warriors = Follower(card_id=10106, title='Horseback Warriors', force=4, chi=0, personal_honor=0, gold_cost=7, focus_value=1, honor_requirement=2, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets a card in this unit: Negate the action's effects on this card."
OYoroi_Troops = Follower(card_id=10107, title='O-Yoroi Troops', force=7, chi=0, personal_honor=0, gold_cost=9, focus_value=4, honor_requirement=2, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After this card bows: Straighten it and, if you do not control a Terrain, negate its <i>(future)</i> straightening until the phase ends.'
Ronin_Ambushers = Follower(card_id=10108, title='Ronin Ambushers', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=3, honor_requirement=0, keywords=[Ronin, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Ninja.'
Water_Spider_Adept = Follower(card_id=10109, title='Water Spider Adept', force=3, chi=0, personal_honor=0, gold_cost=2, focus_value=2, honor_requirement=0, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])