from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, DragonClan
from l5r_auto.keywords import Cavalry, Courtier, Daimyo, Earth, Experienced, Fire, Kensai, Loyal, Magistrate, Monk, Reserve, Samurai, Shugenja, Tattooed, Unique, Void
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'Miroken has +2F while opposing a dishonorable or Gaijin card.'
Kitsuki_Miroken = Personality(card_id=10843, title='Kitsuki Miroken', force=2, chi=4, personal_honor=3, gold_cost=5, honor_requirement=6, clan=[DragonClan], keywords=[Courtier, Magistrate], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy Infantry Personality or Follower -3F.'
Mirumoto_Hatsuto = Personality(card_id=10844, title='Mirumoto Hatsuto', force=2, chi=2, personal_honor=2, gold_cost=5, honor_requirement=0, clan=[DragonClan], keywords=[Cavalry, Kensai, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Fire Battle:</b> Ranged 3 Attack. You may take an additional action to use Kalen's second printed ability.<br><b>Fire Battle, :bow::</b> Ranged 3 Attack."
Mirumoto_Kalen_Experienced = Personality(card_id=10845, title='Mirumoto Kalen', force=4, chi=4, personal_honor=3, gold_cost=11, honor_requirement=2, clan=[DragonClan], keywords=[Cavalry, Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i><br>Enters play for 4 less Gold if you are the Defender.'
Tamori_Shinji = Personality(card_id=10846, title='Tamori Shinji', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=5, clan=[DragonClan], keywords=[Reserve, Earth, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Political Limited:</b> Take the Imperial Favor.'
Togashi_Noboru_Experienced_2 = Personality(card_id=10847, title='Togashi Noboru', force=4, chi=5, personal_honor=3, gold_cost=8, honor_requirement=7, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Experienced('2'), Loyal, Unique, Daimyo, Fire, Monk, Tattooed], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Void Limited:</b> Discard a card to give Obote a Force bonus equal to its Focus Value.'
Togashi_Obote = Personality(card_id=10848, title='Togashi Obote', force=0, chi=2, personal_honor=1, gold_cost=3, honor_requirement=0, clan=[DragonClan, BrotherhoodOfShinsei], keywords=[Monk, Tattooed, Void], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])