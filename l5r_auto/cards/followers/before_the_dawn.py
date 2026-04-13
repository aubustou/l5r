from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Ashigaru, Cavalry, Elite, Ninja, Siege, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Repeatable Battle:</b> Bow one of your Farms to give +1F to each of your Ashigaru Personalities and Followers at the current battlefield.'
Ashigaru_Elite = Follower(card_id=612, title='Ashigaru Elite', force=4, chi=0, personal_honor=0, gold_cost=7, focus_value=2, honor_requirement=1, keywords=[Elite, Unique, Ashigaru], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After this Follower enters play from your hand, create a 0F <b>Ashigaru </b> Follower and attach it to your target Personality.'
Ashigaru_Recruits = Follower(card_id=618, title='Ashigaru Recruits', force=0, chi=0, personal_honor=0, gold_cost=0, focus_value=0, honor_requirement=0, keywords=[Ashigaru], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> After another player's action targets a card in this unit, if you control any Rings, negate the card's bowing from the action's effects."
Brothers_of_Goemon = Follower(card_id=1167, title='Brothers of Goemon', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=4, honor_requirement=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open, :bow::</b> Give a target Province +3 or -3 strength.<br><b>Battle, :bow::</b> Ranged 3 Attack with +1 strength for each other Follower in this unit.'
Genjis_Students = Follower(card_id=2792, title="Genji's Students", force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=1, keywords=[Siege], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After the resolution of your action that bowed, destroyed, or moved a Personality who has opposed this card at the current battlefield: Gain 2 Honor.'
Hida_Defenders = Follower(card_id=3083, title='Hida Defenders', force=2, chi=0, personal_honor=0, gold_cost=2, focus_value=3, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Ranged 4 Attack.'
Horse_Archers = Follower(card_id=3456, title='Horse Archers', force=3, chi=0, personal_honor=0, gold_cost=5, focus_value=2, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Political Open:</b> Bow this card and target a Personality controlled by a player who controls a dishonorable Personality: Give the targeted card a Force penalty equal to his base Personal Honor.'
Rumormonger = Follower(card_id=6404, title='Rumormonger', force=0, chi=0, personal_honor=0, gold_cost=0, focus_value=3, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'As a Focus Effect: You may destroy an attachment on a Personality involved in this duel.<br><b>Battle:</b> Destroy this card and target an enemy card without attachments: Destroy it.'
The_Crimson_Mark = Follower(card_id=8002, title='The Crimson Mark', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=2, honor_requirement=0, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After this card bows: Straighten it.<br><b>Reaction:</b> After another player's action targets a card in this unit: Negate this card's destruction from the action's effects."
Vigilant_Riders = Follower(card_id=9158, title='Vigilant Riders', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=3, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])