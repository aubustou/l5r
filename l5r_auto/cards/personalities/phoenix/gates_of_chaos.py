from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, PhoenixClan
from l5r_auto.keywords import Air, Destined, Earth, ElementalMaster, Expendable, Experienced, Fallen, Fire, GoldenArm, Henshin, Inquisitor, Loyal, Monk, ProtectorOfTheSecondCity, Samurai, Shugenja, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<i>(Draw a card after your Destined card enters play.)</i><br><i>(Draw a card after your Expendable card is destroyed.)</i>'
Asako_Ifukube = Personality(card_id=10648, title='Asako Ifukube', force=0, chi=4, personal_honor=3, gold_cost=6, honor_requirement=12, clan=[PhoenixClan], keywords=[Destined, Expendable, Earth, Inquisitor, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open:</b> Give Karachu Cavalry, Conqueror, or Naval.'
Asako_Karachu_Experienced = Personality(card_id=10647, title='Asako Karachu', force=4, chi=3, personal_honor=2, gold_cost=9, honor_requirement=4, clan=[PhoenixClan, BrotherhoodOfShinsei], keywords=[Unique, Air, Experienced('1'), GoldenArm, Henshin, Monk, ProtectorOfTheSecondCity], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g3:: Give Hajime two +1F <b>Fire </b>tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br>After Hajime enters play, lose 1 Honor.'
Isawa_Hajime = Personality(card_id=10649, title='Isawa Hajime', force=2, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[PhoenixClan], keywords=[Fallen, Fire, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
Isawa_Koizumi = Personality(card_id=10650, title='Isawa Koizumi', force=0, chi=4, personal_honor=2, gold_cost=4, honor_requirement=0, clan=[PhoenixClan], keywords=[Air, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Your other Earth Shugenja have +1F.<br><b>Battle:</b> Give this Province +2 or -2 strength.'
Isawa_Norimichi_Experienced = Personality(card_id=10651, title='Isawa Norimichi', force=4, chi=5, personal_honor=3, gold_cost=9, honor_requirement=8, clan=[PhoenixClan], keywords=[Loyal, Unique, Earth, ElementalMaster, Experienced('1'), Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Expendable card is destroyed.)</i><br><b>Battle:</b> Give a target enemy Personality or Follower -2F.'
Shiba_Tsurao = Personality(card_id=10652, title='Shiba Tsurao', force=4, chi=4, personal_honor=3, gold_cost=8, honor_requirement=6, clan=[PhoenixClan], keywords=[Expendable, Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])