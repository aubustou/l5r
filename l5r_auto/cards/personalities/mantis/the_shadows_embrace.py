from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import MantisClan
from l5r_auto.keywords import Earth, Experienced, Kensai, Kitsune, Magistrate, Naval, Nonhuman, Samurai, Scout, Shugenja, Tactician, Thunder, Unique
from l5r_auto.legality import EmperorEdition, ModernEdition
'<b>Reaction:</b> After Kichi enters play: Create a 3F/2C/3PH <b>Mantis Clan &#149; Nonhuman &#149; Badger &#149; Spirit</b> Personality with the ability, "<b>Battle:</b> Target an enemy Personality: Reduce his Force to 0."'
Kitsune_Kichi = Personality(card_id=9829, title='Kitsune Kichi', force=0, chi=3, personal_honor=3, gold_cost=7, honor_requirement=3, clan=[MantisClan], keywords=[Earth, Kitsune, Nonhuman, Shugenja], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"<b>Battle:</b> Target an opposed attachment: Put it into its owner's hand. You may take an additional Battle action."
Moshi_Rukia = Personality(card_id=9830, title='Moshi Rukia', force=3, chi=3, personal_honor=2, gold_cost=6, honor_requirement=0, clan=[MantisClan], keywords=[Naval, Shugenja, Thunder], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> Ranged 6 Attack that may target a Personality with Followers.'
Tsuruchi_Kosoko_Experienced = Personality(card_id=9831, title='Tsuruchi Kosoko', force=4, chi=4, personal_honor=2, gold_cost=9, honor_requirement=0, clan=[MantisClan], keywords=[Unique, Experienced('1'), Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Battle:</b> One Ranged Attack from your next Ranged Attack action this battle may target a Personality with attached Followers. If you have Reconnaissance, you may take an additional Battle action.'
Yoritomo_Ebumi = Personality(card_id=9832, title='Yoritomo Ebumi', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Other players' Personalities and attachments <i>(in play)</i> have -2 Gold Cost.<br><b>Battle:</b> Target an enemy Personality: Move him home. If he is Crane Clan, bow him."
Yoritomo_Kanahashi = Personality(card_id=9833, title='Yoritomo Kanahashi', force=4, chi=2, personal_honor=1, gold_cost=8, honor_requirement=None, clan=[MantisClan], keywords=[Naval, Magistrate, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Yoritomo_Tsang = Personality(card_id=9834, title='Yoritomo Tsang', force=4, chi=4, personal_honor=2, gold_cost=7, honor_requirement=None, clan=[MantisClan], keywords=[Kensai, Naval, Tactician, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])