from __future__ import annotations
from .common import Follower
from l5r_auto.keywords import Air, Bandit, BattleMaiden, Cat, Cavalry, Earth, Lost, Ninja, Nonhuman, Scout, Shadowlands, Siege, Spirit, Unique, Void
from l5r_auto.legality import CelestialEdition, EmperorEdition, GoldEdition, ImperialEdition, LotusEdition, ModernEdition, SamuraiEdition
'After the resolution of a Ninja action: Give this card +1F.'
Apprentice_Shinobi = Follower(card_id=419, title='Apprentice Shinobi', force=1, chi=0, personal_honor=0, gold_cost=2, focus_value=2, honor_requirement=0, keywords=[Ninja], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Will only attach to a Crane Clan Personality.<br><b>Battle/Open:</b> Target your bowed Personality: Straighten him. Gain 1 Honor.'
Asahina_House_Guard = Follower(card_id=494, title='Asahina House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=2, keywords=[Unique, Air], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Phoenix Clan Personality.<br><b>Battle/Open:</b> Target a Personality: Set his Force equal to his Chi or Personal Honor. Gain 1 Honor.'
Asako_House_Guard = Follower(card_id=543, title='Asako House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=2, keywords=[Unique, Void], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After this Follower enters play, lose 2 Honor. <br>After a battle resolution ends, if this Follower is at the current battlefield, you may pay 2 Gold. If you do not, destroy this Follower.'
Bandit_Gang = Follower(card_id=683, title='Bandit Gang', force=2, chi=0, personal_honor=0, gold_cost=0, focus_value=1, honor_requirement=0, keywords=[Bandit], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, ModernEdition])
"Will only attach to a Spider Clan Personality.<br><b>Ninja Battle:</b> Put this card on the top or bottom of your Fate deck to target an enemy Personality. Put all cards without attachments in his unit on the bottom of their owner's appropriate deck."
Goju_House_Guard = Follower(card_id=2851, title='Goju House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=0, keywords=[Unique, Ninja, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> If you have Reconnaissance: Ranged 4 Attack.'
Hiruma_Sniper = Follower(card_id=3325, title='Hiruma Sniper', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=1, honor_requirement=0, keywords=[Scout], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
"<b>Battle:</b> Destroy this card: Ranged Attack, which may target a Personality with attached Followers, with strength equal to the Chi of the Personality to whom this card was last attached. Lose Honor equal to that Personality's Chi and dishonor him."
Ikiryo = Follower(card_id=3589, title='Ikiryo', force=0, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=0, keywords=[Nonhuman, Shadowlands, Spirit], traits=[], abilities=[], legality=[EmperorEdition, ImperialEdition, GoldEdition, ModernEdition])
"Will only attach to a Lion Clan Personality.<br><b>Battle:</b> Melee Attack with strength equal to this Personality's Personal Honor plus two. If this Melee Attack destroyed a card, gain 1 Honor."
Ikoma_House_Guard = Follower(card_id=3611, title='Ikoma House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=2, keywords=[Unique, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Crab Clan Personality.<br><b>Battle:</b> Target an enemy card without attachments whose unit has lower total Force than this unit: Destroy the target. Gain 1 Honor.'
Kaiu_House_Guard = Follower(card_id=4118, title='Kaiu House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=0, keywords=[Unique, Siege], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 4 Attack.<br><b>Reaction:</b> If this card is at the current battlefield, after a Ranged Attack is targeted: Give it +2 strength.'
Khol_Regulars = Follower(card_id=4338, title='Khol Regulars', force=5, chi=0, personal_honor=0, gold_cost=8, focus_value=2, honor_requirement=1, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'After this card enters play: Lose 2 Honor. <br>Actions performed by Personalities with a Gold Cost of 7 or lower may not target this Personality.'
Legion_of_Pain = Follower(card_id=4699, title='Legion of Pain', force=5, chi=0, personal_honor=0, gold_cost=6, focus_value=3, honor_requirement=0, keywords=[Lost, Shadowlands], traits=[], abilities=[], legality=[EmperorEdition, LotusEdition, ModernEdition])
'Will only attach to a Unicorn Clan Personality.<br><b>Battle:</b> If any enemy units are at the current battlefield: Move this Personality there. If he is now there, Ranged 4 Attack.'
Moto_House_Guard = Follower(card_id=5329, title='Moto House Guard', force=3, chi=0, personal_honor=0, gold_cost=5, focus_value=4, honor_requirement=1, keywords=[Cavalry, Unique], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Outriders = Follower(card_id=5837, title='Outriders', force=3, chi=0, personal_honor=0, gold_cost=3, focus_value=3, honor_requirement=0, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Shinjos_Children = Follower(card_id=6975, title="Shinjo's Children", force=4, chi=0, personal_honor=0, gold_cost=5, focus_value=2, honor_requirement=2, keywords=[Cavalry], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])
'Will only attach to a Scorpion Clan Personality.<br><b>Political Battle/Open:</b> Target a Personality: If it is a Combat Segment, bow him. If he is dishonorable, his controller loses 1 Honor.'
Soshi_House_Guard = Follower(card_id=7347, title='Soshi House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=0, keywords=[Unique, Ninja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Melee 6 Attack.'
Stalking_Tiger = Follower(card_id=7450, title='Stalking Tiger', force=4, chi=0, personal_honor=0, gold_cost=7, focus_value=2, honor_requirement=0, keywords=[Cat, Nonhuman], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Dragon Clan Personality.<br><b>Battle:</b> Target an enemy Personality or Follower: It is encased in stone. Give it -4F. It may not perform actions.'
Tamori_House_Guard = Follower(card_id=7776, title='Tamori House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=1, keywords=[Unique, Earth], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Will only attach to a Mantis Clan Personality.<br><b>Battle:</b> Ranged 5 Attack that you may compare against Gold Cost.'
Tsuruchi_House_Guard = Follower(card_id=8837, title='Tsuruchi House Guard', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=4, honor_requirement=0, keywords=[Unique, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Battle Maidens in this army have +1F while attacking.'
Utaku_Elite_Guard = Follower(card_id=9058, title='Utaku Elite Guard', force=1, chi=0, personal_honor=0, gold_cost=3, focus_value=2, honor_requirement=3, keywords=[Cavalry, BattleMaiden], traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
'<b>Battle:</b> Draw a card.'
Veteran_Advisor = Follower(card_id=9144, title='Veteran Advisor', force=4, chi=0, personal_honor=0, gold_cost=7, focus_value=2, honor_requirement=1, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, SamuraiEdition, ModernEdition])
Veteran_Skirmishers = Follower(card_id=9147, title='Veteran Skirmishers', force=3, chi=0, personal_honor=0, gold_cost=2, focus_value=3, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Reaction:</b> After this card enters play from your hand: Draw one card for each player who has had a province destroyed this game.'
Village_Guardian = Follower(card_id=9162, title='Village Guardian', force=3, chi=0, personal_honor=0, gold_cost=4, focus_value=1, honor_requirement=0, traits=[], abilities=[], legality=[EmperorEdition, CelestialEdition, ModernEdition])