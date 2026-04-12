from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import NinjaFaction, ScorpionClan
from l5r_auto.keywords import Actor, Artisan, Courtier, Expendable, Experienced, Loyal, Magistrate, Ninja, Paragon, Reserve, Samurai, Siege, Tactician, Unique, Yojimbo
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Siege Battle, :bow::</b> Ranged 3 Attack. If this destroyed a card, give this Province +2 or -2 strength.'
Bayushi_Dijuro = Personality(card_id=10867, title='Bayushi Dijuro', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=None, clan=[ScorpionClan], keywords=[Tactician, Unique, Samurai, Siege], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Will not attach Armor.<br><b>Ninja Open, :bow::</b> Give a target Personality and Jin-e each a -1F/-1C <b>Poison </b>token.'
Bayushi_Jine = Personality(card_id=10868, title='Bayushi Jin-e', force=2, chi=4, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Give a target enemy Personality -3F.'
Bayushi_Mifuyu = Personality(card_id=10869, title='Bayushi Mifuyu', force=4, chi=3, personal_honor=1, gold_cost=7, honor_requirement=None, clan=[ScorpionClan], keywords=[Magistrate, Samurai], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<i>(You may Recruit a Reserve card, if it would be opposed, as an <b>Absent Battle</b> action.)</i><br><b>Ninja Absent Interrupt:</b> After you Recruit Wateru during battle, take an additional Battle action.'
Bayushi_Wateru = Personality(card_id=10870, title='Bayushi Wateru', force=4, chi=3, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Reserve, Ninja, Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Open:</b> Discard a card to give a target Personality a Force or Personal Honor bonus equal to the card's Focus Value. The target has a maximum Personal Honor of 4."
Shosuro_Chizuru = Personality(card_id=10871, title='Shosuro Chizuru', force=0, chi=1, personal_honor=0, gold_cost=4, honor_requirement=None, clan=[ScorpionClan], keywords=[Loyal, Actor, Artisan], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<i>(Draw a card after your Expendable card is destroyed.)</i><br><b>Political Engage:</b> Other players do not gain Honor for destroying your cards in this battle's resolution."
Shosuro_Takazaki = Personality(card_id=10872, title='Shosuro Takazaki', force=0, chi=3, personal_honor=0, gold_cost=3, honor_requirement=None, clan=[ScorpionClan, NinjaFaction], keywords=[Expendable, Courtier, Ninja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"While you control a Courtier, The Sorrow's printed ability is <b>Battle/Limited</b>.<br><b>Battle:</b> Give a target Personality -4F."
The_Sorrow_Experienced = Personality(card_id=10873, title='The Sorrow', force=4, chi=3, personal_honor=3, gold_cost=8, honor_requirement=0, clan=[ScorpionClan], keywords=[Experienced('Bayushi Tenzan'), Loyal, Unique, Magistrate, Paragon, Samurai, Yojimbo], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])