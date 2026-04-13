from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Cavalry, Elephant, Nikutai, Ninja, Nonhuman, Scout
from l5r_auto.legality import EmperorEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'After this Follower enters play from your hand, draw an additional card before your next turn ends.'
Clearing_Crew = Follower(card_id=9867, title='Clearing Crew', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=2, honor_requirement=1, keywords=[Ashigaru], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Fear Battle:</b> Target an enemy card with equal or lower Force. If it is bowed or an attachment, destroy it. Bow it.'
Elephant_Caravan = Follower(card_id=9868, title='Elephant Caravan', force=5, chi=0, personal_honor=0, gold_cost=9, focus_value=1, honor_requirement=0, keywords=[Cavalry, Elephant, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> If this card is opposed, discard a card: Give this card +3F.'
Heavy_Chargers = Follower(card_id=9869, title='Heavy Chargers', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Will only attach to a Ninja.<br><b>Ninja Interrupt:</b> A single Ranged Attack from the action may target an otherwise legal card in the Defender's home. Destroy this Follower."
Lookout = Follower(card_id=9870, title='Lookout', force=3, chi=0, gold_cost=4, focus_value=2, keywords=[Ninja], traits=[], abilities=[], legality=[TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
Native_Guide = Follower(card_id=9871, title='Native Guide', force=5, chi=0, personal_honor=0, gold_cost=6, focus_value=3, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Tireless Reaction:</b> After a Follower in this unit bows: Straighten it.<br><b>Battle:</b> Melee 5 Attack.'
Nikutai = Follower(card_id=9872, title='Nikutai', force=5, chi=0, personal_honor=0, gold_cost=8, focus_value=3, honor_requirement=2, keywords=[Nikutai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"This Personality may not be assigned to, and will not move into, an attacking army.<br>Melee and Ranged Attacks targeting cards in this unit have -3 strength.<br><b>Reaction:</b> After another player's action resolves which destroyed another card in this unit: Gain 2 Honor."
Shieldman = Follower(card_id=9873, title='Shieldman', force=3, chi=0, personal_honor=0, gold_cost=0, focus_value=3, honor_requirement=1, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Recon Reaction:</b> After engaging at this card's battlefield: You have Reconnaissance there. Give your other Followers there +1F."
Wasteland_Scout = Follower(card_id=9874, title='Wasteland Scout', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=1, keywords=[Cavalry, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])