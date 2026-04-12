from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import CraneClan, SpiritFaction
from l5r_auto.keywords import Air, Artisan, Courtier, Duelist, Experienced, IronCrane, Kodama, Magistrate, Merchant, Nonhuman, Samurai, Scout, Shugenja, Spirit, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Limited:</b> Bow your target Temple: Draw a card.'
Asahina_Keigo_Experienced = Personality(card_id=9810, title='Asahina Keigo', force=2, chi=4, personal_honor=3, gold_cost=7, honor_requirement=10, clan=[CraneClan], keywords=[Unique, Air, Experienced('1'), Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Favor Political Open:</b> Discard the Imperial Favor to target a Personality. <i>Sosuke raises tariffs.</i> Bow a card without attachments in the target's unit, or bow his unit if he is Mantis Clan."
Daidoji_Sosuke = Personality(card_id=9811, title='Daidoji Sosuke', force=2, chi=4, personal_honor=4, gold_cost=8, honor_requirement=6, clan=[CraneClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Daidoji_Tsunehiko = Personality(card_id=9812, title='Daidoji Tsunehiko', force=6, chi=3, personal_honor=2, gold_cost=8, honor_requirement=0, clan=[CraneClan], keywords=[IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'After Ichigiku challenges a dishonorable Personality during a Combat Segment, the challenge will not be refused; destroy the loser in addition to other consequences of losing.'
Kakita_Ichigiku = Personality(card_id=9813, title='Kakita Ichigiku', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[CraneClan], keywords=[Duelist, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Target your Personality: Create a +2F <b>Armor</b> Item with the trait, "Melee and Ranged Attacks targeting this Personality have -3 strength" and attach it to him.'
Kakita_Saki = Personality(card_id=9814, title='Kakita Saki', force=1, chi=3, personal_honor=2, gold_cost=5, honor_requirement=5, clan=[CraneClan], keywords=[Artisan], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Iaijutsu Battle/Limited:</b> Target another player's Personality: Tadanobu duels him. If it is your turn, the winner's controller draws a card. Bow the duel's loser."
Kakita_Tadanobu_Experienced = Personality(card_id=9815, title='Kakita Tadanobu', force=2, chi=5, personal_honor=4, gold_cost=9, honor_requirement=10, clan=[CraneClan], keywords=[Duelist, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Your maximum hand size is increased by one.'
Kazehime = Personality(card_id=9816, title='Kazehime', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[CraneClan, SpiritFaction], keywords=[Air, Kodama, Nonhuman, Shugenja, Spirit], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])