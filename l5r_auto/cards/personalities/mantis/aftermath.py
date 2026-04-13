from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Air, Courtier, Destined, Earth, Experienced, Fire, GoMaster, IvoryChampionsAdvisor, Magistrate, Naval, Reserve, Samurai, Scout, Shugenja, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'Your Nonhuman Spirits have the ability, "<b>Battle, :bow::</b> Ranged 3 Attack."'
Kitsune_Merihiko_Experienced = Personality(card_id=10855, title='Kitsune Merihiko', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=5, clan=[MantisClan], keywords=[Unique, Earth, Experienced('1'), IvoryChampionsAdvisor, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Interrupt:</b> After you Recruit Yamazaru, create a 3F/2C/3PH <b>Mantis Clan &#149; Monkey &#149; Nonhuman &#149; Spirit</b> Personality with the ability, "<b>Battle:</b> Discard a card to give a target enemy Personality or Follower a Force penalty equal to the card\'s Focus Value."'
Kitsune_Yamazaru = Personality(card_id=10856, title='Kitsune Yamazaru', force=0, chi=3, personal_honor=3, gold_cost=6, honor_requirement=2, clan=[MantisClan], keywords=[Earth, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i><br><b>Fire Battle:</b> Ranged 1 Attack.'
Moshi_Ikako = Personality(card_id=10857, title='Moshi Ikako', force=3, chi=3, personal_honor=2, gold_cost=7, honor_requirement=0, clan=[MantisClan], keywords=[Naval, Reserve, Air, Fire, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br><b>Repeatable Battle, :g2::</b> Give Shusaku +1F. <i>(Repeatable actions may be used any number of times per turn.)</i>'
Tsuruchi_Shusaku = Personality(card_id=10858, title='Tsuruchi Shusaku', force=1, chi=2, personal_honor=1, gold_cost=4, honor_requirement=None, clan=[MantisClan], keywords=[Destined, GoMaster, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g5:: Give Toganin three +1F tokens. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br>Toganin has +1F if any other player is Crane Clan.'
Yoritomo_Toganin = Personality(card_id=10859, title='Yoritomo Toganin', force=2, chi=3, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Crane Clan players may Proclaim Yashinko.<br><b>:bow::</b> Produce 3 Gold.'
Yoritomo_Yashinko_Experienced = Personality(card_id=10860, title='Yoritomo Yashinko', force=0, chi=3, personal_honor=2, gold_cost=4, honor_requirement=None, clan=[MantisClan], keywords=[Unique, Courtier, Experienced('1')], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])