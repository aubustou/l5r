from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Commander, Experienced, HeadOfTheSecondCityGuardsmen, Paragon, Samurai, Scout, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle:</b> Even if Tsudoken is bowed: Straighten him. He rallies the guards. You may target a Personality and bow or straighten him.'
Akodo_Tsudoken_Experienced = Personality(card_id=302, title='Akodo Tsudoken', force=5, chi=3, personal_honor=4, gold_cost=9, honor_requirement=7, clan=[LionClan], keywords=[Tactician, Unique, Commander, Experienced('1'), HeadOfTheSecondCityGuardsmen, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Battle:</b> Target a card in a unit; the card must have no attachments unless you control a Terrain: Bow or straighten the card.'
Ikoma_Tsukasa = Personality(card_id=3655, title='Ikoma Tsukasa', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After Kagako enters play: She summons an ancestor. Create a 2F/2C/3PH <b>Lion Clan &#149; Samurai &#149; Ancestor &#149; Spirit</b> Personality. Gain 1 Honor.'
Kitsu_Kagako = Personality(card_id=4382, title='Kitsu Kagako', force=1, chi=4, personal_honor=3, gold_cost=6, honor_requirement=4, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Target an enemy unit: Reduce the Force of each Personality and Follower in it by Koyama's Personal Honor. Bow any cards in the unit whose Force is now 0."
Matsu_Koyama = Personality(card_id=4944, title='Matsu Koyama', force=4, chi=3, personal_honor=4, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])