from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Cavalry, Destined, Experienced, Imperial, ImperialExplorer, MasterTactician, Naval, Paragon, Reserve, Samurai, Scout, Shugenja, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
"Kano's Force bonuses from the rulebook Tactical Advantage action are increased by 2."
Akodo_Kano_Experienced = Personality(card_id=10849, title='Akodo Kano', force=3, chi=4, personal_honor=3, gold_cost=7, honor_requirement=10, clan=[LionClan], keywords=[Tactician, Unique, Experienced('1'), MasterTactician, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Limited:</b> Put a target Terrain from your discard pile into your hand. Discard a card.'
Akodo_Uehara_Experienced = Personality(card_id=10850, title='Akodo Uehara', force=2, chi=3, personal_honor=2, gold_cost=7, honor_requirement=6, clan=[LionClan], keywords=[Tactician, Unique, Experienced('1'), Imperial, ImperialExplorer, Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
Ikoma_Takakura = Personality(card_id=10851, title='Ikoma Takakura', force=3, chi=3, personal_honor=2, gold_cost=4, honor_requirement=4, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Interrupt:</b> After you Recruit Tamao, create a 2F/2C/3PH <b>Lion Clan &#149; Ancestor &#149; Samurai &#149; Spirit</b> Personality.'
Kitsu_Tamao = Personality(card_id=10852, title='Kitsu Tamao', force=0, chi=3, personal_honor=2, gold_cost=5, honor_requirement=3, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Battle:</b> Give a target enemy Personality or Follower a Force penalty equal to Miura's Personal Honor."
Matsu_Miura = Personality(card_id=10853, title='Matsu Miura', force=3, chi=3, personal_honor=3, gold_cost=6, honor_requirement=7, clan=[LionClan], keywords=[Naval, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i><br><i>(Draw a card after your Destined card enters play.)</i>'
Matsu_Ryohei = Personality(card_id=10854, title='Matsu Ryohei', force=2, chi=1, personal_honor=3, gold_cost=6, honor_requirement=7, clan=[LionClan], keywords=[Cavalry, Destined, Reserve, Paragon, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])