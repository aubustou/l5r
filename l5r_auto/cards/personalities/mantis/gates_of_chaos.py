from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan, SpiritFaction
from l5r_auto.keywords import Charitable, ClanChampion, Conqueror, Destined, Earth, Experienced, Fallen, Kensai, Kitsune, Loyal, Magistrate, Naval, Nonhuman, Samurai, Scout, Shugenja, Spirit, TheGrowingStorm, Thunder, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'Invest :g2:: Gain 1 Honor. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br><b>Limited, :bow::</b> Gain 1 Honor.'
Kitsune_Yuko = Personality(card_id=10641, title='Kitsune Yuko', force=1, chi=4, personal_honor=3, gold_cost=6, honor_requirement=2, clan=[MantisClan, SpiritFaction], keywords=[Earth, Kitsune, Nonhuman, Shugenja, Spirit], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Bow a target enemy card without attachments. Destroy it if it is an attachment.'
Moshi_Rukia_Experienced = Personality(card_id=10642, title='Moshi Rukia', force=3, chi=4, personal_honor=2, gold_cost=8, honor_requirement=2, clan=[MantisClan], keywords=[Naval, Unique, Experienced('1'), Shugenja, Thunder], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Tireless Battle:</b> Straighten Sasako. <i>(Tireless actions may be taken while bowed.)</i>'
Moshi_Sasako_Experienced = Personality(card_id=10643, title='Moshi Sasako', force=4, chi=4, personal_honor=1, gold_cost=10, honor_requirement=None, clan=[MantisClan], keywords=[Conqueror, Naval, Unique, Experienced('1'), Shugenja, Thunder], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Gombei enters play, lose 1 Honor.'
Tsuruchi_Gombei = Personality(card_id=10644, title='Tsuruchi Gombei', force=3, chi=1, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Fallen, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle, :gstar::</b> Ranged Attack with strength equal to the Gold paid.'
Yoritomo_Hiromi_Experienced = Personality(card_id=10646, title='Yoritomo Hiromi', force=5, chi=5, personal_honor=3, gold_cost=14, honor_requirement=5, clan=[MantisClan], keywords=[Kensai, Loyal, Naval, Unique, ClanChampion, Experienced('1'), Samurai, TheGrowingStorm, Thunder], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br><b>Limited, :gstar::</b> Recruit a target Holding in your Province <i>(entering play bowed)</i>, for 1 less Gold.'
Yoritomo_Mikaru = Personality(card_id=10645, title='Yoritomo Mikaru', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Destined, Charitable, Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])