from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import AdvisorToTheRubyChampion, Berserker, Commander, Courtier, CrimeBoss, Daimyo, Experienced, Hero, Jade, Kolat, Loyal, MasterCoin, Merchant, Samurai, Scout, Siege, Tactician, Unique
from l5r_auto.legality import CelestialEdition, EmperorEdition, ModernEdition
'<b>Battle:</b> Target a bowed enemy card: Destroy it.'
Hida_Mimori = Personality(card_id=3150, title='Hida Mimori', force=8, chi=2, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[CrabClan], keywords=[Berserker], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Reaction:</b> Twice per turn, after an action targets your Follower at Mochitoko's location: Negate its bowing and destruction from that action's effects."
Hida_Mochitoko_Experienced = Personality(card_id=3152, title='Hida Mochitoko', force=6, chi=3, personal_honor=2, gold_cost=9, honor_requirement=0, clan=[CrabClan], keywords=[Unique, AdvisorToTheRubyChampion, Commander, Experienced('1'), Hero, Jade, Samurai], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> If you have Reconnaissance: Ranged 4 Attack.<br><b>Battle:</b> Bow your performing Follower in Tensin's unit: Ranged 4 Attack."
Hiruma_Tensin = Personality(card_id=3332, title='Hiruma Tensin', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[CrabClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
Kaiu_Watsuki = Personality(card_id=4150, title='Kaiu Watsuki', force=3, chi=3, personal_honor=3, gold_cost=6, honor_requirement=3, clan=[CrabClan], keywords=[Tactician, Samurai, Siege], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Political Open:</b> Target a Holding or Stronghold: Straighten it.<br><b>Political Reaction:</b> After an action targets your Merchant, pay 2 Gold: Negate the action's effects."
Yasuki_JinnKuen_Experienced_2 = Personality(card_id=9445, title='Yasuki Jinn-Kuen', force=2, chi=4, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan], keywords=[Experienced('2'), Loyal, Unique, Courtier, Daimyo, Kolat, MasterCoin, Merchant], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'<b>Reaction:</b> After Tsujiken enters play, target a Holding: Until Tsujiken leaves play, after each time its controller bows it, he loses 1 Honor.<br><b>Open:</b> Bow Tsujiken and target a Holding: Straighten it. You may bow it if its base Gold Cost is 4 or lower.'
Yasuki_Tsujiken = Personality(card_id=9469, title='Yasuki Tsujiken', force=3, chi=4, personal_honor=0, gold_cost=10, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, CrimeBoss, Merchant], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])