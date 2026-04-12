from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CrabClan
from l5r_auto.keywords import Berserker, Brash, Courtier, Experienced, FavoredOfTheVoidDragon, Fudo, JadeHand, Merchant, Mutant, Nonhuman, Oyabun, Samurai, Scout, Siege, Tactician, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
"Before the first time each turn another player's action moves Kaiji: Negate his movement from that action.<br><b>Battle:</b> Target an enemy card with lower Force: Bow it. Destroy it if it has no attachments."
Hida_Kaiji = Personality(card_id=10040, title='Hida Kaiji', force=9, chi=2, personal_honor=0, gold_cost=12, honor_requirement=None, clan=[CrabClan], keywords=[Berserker, Mutant, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 6 Attack.<br><b>Battle:</b> Target an enemy card with the base Shadowlands keyword: Destroy it.'
Hiruma_Nitani_Experienced = Personality(card_id=10041, title='Hiruma Nitani', force=5, chi=3, personal_honor=3, gold_cost=9, honor_requirement=3, clan=[CrabClan], keywords=[Unique, Experienced('1'), JadeHand, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Target two Personalities controlled by the same player: Transfer a Follower from one to the other. If you have Reconnaissance, you may take an additional action.'
Hiruma_Sawai = Personality(card_id=10042, title='Hiruma Sawai', force=3, chi=2, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[CrabClan], keywords=[Fudo, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<i>(The Defender may draw a card after a Brash card is assigned to attack.)</i><br><b>Battle:</b> Target an enemy Personality or Follower: Give it -3F. You may take an additional Battle action.'
Kaiu_Okaru = Personality(card_id=10043, title='Kaiu Okaru', force=4, chi=3, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[CrabClan], keywords=[Brash, Tactician, Samurai, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Favor Political Limited:</b> Discard the Imperial Favor to target a dishonorable Personality. His controller loses 1 Honor.<br><b>Political Open, :g2::</b> Take the Imperial Favor.'
Yasuki_Baiko = Personality(card_id=10044, title='Yasuki Baiko', force=0, chi=3, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[CrabClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Open:</b> Target a Holding or your Stronghold: Bow or straighten it.<br><b>Limited:</b> Pay 5 Gold: Draw a card.<br><b>Limited:</b> Bow Tsujiken and target a Personality: Dishonor him. His controller loses 1 Honor.'
Yasuki_Tsujiken_Experienced = Personality(card_id=10045, title='Yasuki Tsujiken', force=3, chi=5, personal_honor=0, gold_cost=11, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Courtier, Experienced('1'), FavoredOfTheVoidDragon, Merchant, Oyabun], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])