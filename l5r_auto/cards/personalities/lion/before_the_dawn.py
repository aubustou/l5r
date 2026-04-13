from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Commander, Deathseeker, Experienced, Hero, Legendary, Lion, Nonhuman, Paragon, Samurai, Scout, Tactician, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle, :gstar::</b> If Ashiko is face-up in one of your Provinces, Recruit her reducing her Gold Cost by 2 if there are more units on the enemy side of the current battle than on your side.'
Akodo_Ashiko = Personality(card_id=193, title='Akodo Ashiko', force=5, chi=4, personal_honor=0, gold_cost=8, honor_requirement=0, clan=[LionClan], keywords=[Deathseeker, Hero, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"After the resolution of your Tactical action, give Kobi +1F.<br><b>Reaction:</b> After another player's Battle action resolves which destroyed one of your Lion Clan Personalities at the current battlefield, before the current turn ends, if the destroyed Personality is dead, Recruit him, ignoring costs and Honor Requirements."
Akodo_Kobi_Experienced = Personality(card_id=232, title='Akodo Kobi', force=4, chi=5, personal_honor=3, gold_cost=9, honor_requirement=0, clan=[LionClan], keywords=[Tactician, Unique, Experienced('1'), Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle/Open:</b> Discard a card and target a Bushido Virtue in your discard pile: Take an additional action to play it for one of its Battle, Limited, or Open actions, as appropriate to the current phase. Remove it from the game after its action ends.'
Akodo_Tezuka = Personality(card_id=298, title='Akodo Tezuka', force=4, chi=2, personal_honor=4, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> Even if Ayumu is bowed, after you announce a Tactical action, if he is at the current battlefield: Straighten him.'
Ikoma_Ayumu = Personality(card_id=3595, title='Ikoma Ayumu', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target a Follower in your hand and one of your Personalities: Attach the Follower to the Personality, paying all costs.'
Ikoma_Shinohara = Personality(card_id=3639, title='Ikoma Shinohara', force=4, chi=2, personal_honor=3, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Commander, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Kaido has +1F while attacking.<br><b>Fear Battle:</b> Target an enemy Personality or Follower: Reduce its Force to 0.'
Matsu_Kaido = Personality(card_id=4934, title='Matsu Kaido', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=4, clan=[LionClan], keywords=[Hero, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Pride of the Hand has +1F while you control a Terrain at its battlefield.'
Pride_of_the_Hand = Personality(card_id=6064, title='Pride of the Hand', force=3, chi=2, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[LionClan], keywords=[Legendary, Lion, Nonhuman, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])