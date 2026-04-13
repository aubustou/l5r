from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, CraneClan
from l5r_auto.keywords import Air, Cavalry, Commander, Courtier, Destined, Duelist, Experienced, Fallen, FavoredOfTheAirDragon, IronCrane, Magistrate, Merchant, Monk, Samurai, Scout, Shugenja, Unique
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>Limited, :bow::</b> Search your discard pile, then Fate deck, for a Ring. Show it and put it in your hand. Discard a card.'
Asahina_Kitiaru_Experienced = Personality(card_id=10623, title='Asahina Kitiaru', force=0, chi=5, personal_honor=4, gold_cost=7, honor_requirement=10, clan=[CraneClan, BrotherhoodOfShinsei], keywords=[Unique, Courtier, Experienced('1'), Monk], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open, :bow::</b> Target one or two of your Provinces. After the first time this turn a Personality attacks one of those Provinces, gain 2 Honor.'
Asahina_Shigemitsu_Experienced = Personality(card_id=10624, title='Asahina Shigemitsu', force=2, chi=5, personal_honor=4, gold_cost=8, honor_requirement=10, clan=[CraneClan], keywords=[Cavalry, Unique, Air, Experienced('1'), FavoredOfTheAirDragon, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 3 Gold.'
Daidoji_Soken = Personality(card_id=10625, title='Daidoji Soken', force=0, chi=3, personal_honor=3, gold_cost=6, honor_requirement=4, clan=[CraneClan], keywords=[Courtier, Merchant], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Tametaka loses any duel against Yoritomo Hiromi.<br><b>Battle:</b> Reduce the Force of a target enemy Personality or Follower to 0.'
Daidoji_Tametaka_Experienced = Personality(card_id=10627, title='Daidoji Tametaka', force=4, chi=3, personal_honor=2, gold_cost=8, honor_requirement=4, clan=[CraneClan], keywords=[Unique, Commander, Experienced('1'), IronCrane, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(Draw a card after your Destined card enters play.)</i><br>After Tobei enters play, lose 1 Honor.<br><b>Battle, :bow::</b> Ranged 2 Attack.'
Daidoji_Tobei = Personality(card_id=10628, title='Daidoji Tobei', force=3, chi=2, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[CraneClan], keywords=[Destined, Fallen, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Invest :g1:: Give Razan a +1C token. <i>(After this card enters play, you may also pay the Invest cost to get the effect, once.)</i><br><b>Limited:</b> Destroy a target Fudo card. Destroy Razan.'
Doji_Razan = Personality(card_id=10626, title='Doji Razan', force=2, chi=3, personal_honor=3, gold_cost=5, honor_requirement=2, clan=[CraneClan], keywords=[Duelist, Courtier, Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])