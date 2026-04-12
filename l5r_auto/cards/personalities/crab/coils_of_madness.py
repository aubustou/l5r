from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, CrabClan
from l5r_auto.keywords import Berserker, Bully, Courtier, Daimyo, Earth, Experienced, Fallen, Inexperienced, Jade, Loyal, Magistrate, Merchant, Monk, Samurai, Scout, Shugenja, TheFleshEater, TheRazorsEdge, TheSteelEyed, TortoiseClan, Unique, WitchHunter
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'<b>Limited:</b> Bow a target Personality with lower Force.'
Hida_OUshi_Inexperienced = Personality(card_id=10437, title='Hida O-Ushi', force=3, chi=2, personal_honor=1, gold_cost=6, honor_requirement=None, clan=[CrabClan], keywords=[Loyal, Unique, Bully, Inexperienced, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Nikaru enters play, lose 3 Honor.<br>Nikaru uses his printed Force as his duel stat.'
Hiruma_Nikaru_the_Flesh_Eater_Experienced_2 = Personality(card_id=10438, title='Hiruma Nikaru, the Flesh Eater', force=9, chi=2, personal_honor=0, gold_cost=11, honor_requirement=None, clan=[CrabClan], keywords=[Experienced('2'), Unique, Berserker, Fallen, TheFleshEater], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Ogata enters play, lose 2 Honor.<br>Ogata has +1F for each opposing Madness token.'
Hiruma_Ogata = Personality(card_id=10441, title='Hiruma Ogata', force=3, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[CrabClan], keywords=[Fallen, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>:bow::</b> Produce 1 Gold.'
Kasuga_Aizawa_the_Razors_Edge = Personality(card_id=10439, title="Kasuga Aizawa, the Razor's Edge", force=0, chi=2, personal_honor=1, gold_cost=2, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Merchant, TheRazorsEdge, TortoiseClan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Renyu enters play, create a 1F <b>Dog &#149; Nonhuman</b> Follower and attach it to him.<br><b>Earth Battle:</b> Bow a target enemy card with Shadowlands or without attachments.'
Kuni_Renyu_Experienced_2 = Personality(card_id=10440, title='Kuni Renyu', force=5, chi=5, personal_honor=3, gold_cost=10, honor_requirement=None, clan=[CrabClan], keywords=[Experienced('2'), Loyal, Unique, Daimyo, Earth, Jade, Magistrate, Shugenja, WitchHunter], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Nishoji enters play ignoring Gold Cost if you control the Ring of Earth.<br>Nishoji uses his printed Force as his duel stat.'
Nishoji_the_SteelEyed = Personality(card_id=10442, title='Nishoji, the Steel-Eyed', force=6, chi=2, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[CrabClan, BrotherhoodOfShinsei], keywords=[Unique, Earth, Monk, TheSteelEyed], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Open, :bow::</b> Straighten a target Holding or Shosuro Kameyoi.'
Yasuki_Tono_Experienced = Personality(card_id=10443, title='Yasuki Tono', force=2, chi=3, personal_honor=1, gold_cost=5, honor_requirement=None, clan=[CrabClan], keywords=[Unique, Courtier, Experienced('1'), Merchant], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])