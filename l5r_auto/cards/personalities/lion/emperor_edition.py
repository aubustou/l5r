from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import LionClan
from l5r_auto.keywords import Cavalry, ClanChampion, Commander, Justicar, Loyal, MasterTactician, Paragon, Samurai, Scout, Shugenja, SodanSenzo, SoulOf, Tactician, Unique, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
"<b>Tireless Reaction:</b> <i>Dairuko rallies her troops.</i> Before the resolution of a battle at her battlefield, that battle's resolution will not bow cards in your army.<br><b>Battle:</b> Melee 8 Attack."
Akodo_Dairuko = Personality(card_id=200, title='Akodo Dairuko', force=6, chi=5, personal_honor=5, gold_cost=10, honor_requirement=10, clan=[LionClan], keywords=[Loyal, Tactician, Unique, ClanChampion, Paragon, Samurai], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Give Kano a <b>Master </b>token.<br><b>Battle, :bow::</b> Destroy a Master token on Kano to take two additional Battle actions.'
Akodo_Kano = Personality(card_id=226, title='Akodo Kano', force=2, chi=4, personal_honor=3, gold_cost=6, honor_requirement=8, clan=[LionClan], keywords=[Tactician, Unique, MasterTactician, Samurai, SoulOf('Kitsu Motso')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Akodo_Kisho = Personality(card_id=229, title='Akodo Kisho', force=3, chi=3, personal_honor=4, gold_cost=5, honor_requirement=10, clan=[LionClan], keywords=[Commander, Paragon, Samurai, SoulOf('Akodo Dosei')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Tactical Limited:</b> Create a 2F Follower and attach it to Makotai.'
Akodo_Makotai = Personality(card_id=241, title='Akodo Makotai', force=3, chi=3, personal_honor=2, gold_cost=8, honor_requirement=3, clan=[LionClan], keywords=[Tactician, Commander, Samurai, SoulOf('Akodo Mirotai')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Akodo_Suoh = Personality(card_id=288, title='Akodo Suoh', force=2, chi=2, personal_honor=2, gold_cost=5, honor_requirement=6, clan=[LionClan], keywords=[Tactician, Samurai, SoulOf('Akodo Shunori')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Natsu will not be controlled by a Unicorn Clan player.'
Ikoma_Natsu = Personality(card_id=3623, title='Ikoma Natsu', force=3, chi=2, personal_honor=2, gold_cost=5, honor_requirement=8, clan=[LionClan], keywords=[Cavalry, Samurai, SoulOf('Ikoma Otemi')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Ikoma_Shika = Personality(card_id=3636, title='Ikoma Shika', force=2, chi=2, personal_honor=2, gold_cost=2, honor_requirement=4, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Battle:</b> Target a Terrain and an enemy card without attachments: Destroy both targets.'
Ikoma_Shinju = Personality(card_id=3638, title='Ikoma Shinju', force=4, chi=3, personal_honor=2, gold_cost=7, honor_requirement=2, clan=[LionClan], keywords=[Samurai, Scout], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
Kitsu_Sorano = Personality(card_id=4395, title='Kitsu Sorano', force=0, chi=3, personal_honor=3, gold_cost=3, honor_requirement=3, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> Each player who controls an Ancestor gains 1 Honor. For any player who controls no Ancestors and has higher Honor than his starting Family Honor, you may choose to have him lose 1 Honor.'
Kitsu_Suki = Personality(card_id=4396, title='Kitsu Suki', force=0, chi=4, personal_honor=3, gold_cost=6, honor_requirement=6, clan=[LionClan], keywords=[Shugenja, Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
"<b>Reaction:</b> After Tamasine enters play: Create a 2F/2C/3PH <b>Lion Clan &#149; Samurai &#149; Ancestor &#149; Spirit</b> Personality.<br><b>Battle:</b> Bow Tamasine and target your Ancestor, or one to four of your Ancestors if you have lost Honor from another player's action during an Action Phase since your last turn began: Give each target +4F."
Kitsu_Tamasine = Personality(card_id=4397, title='Kitsu Tamasine', force=2, chi=4, personal_honor=4, gold_cost=8, honor_requirement=7, clan=[LionClan], keywords=[Shugenja, SodanSenzo, Water], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
"Arata has +2F while attacking.<br><b>Battle:</b> Target an enemy Personality or Follower: Give it a Force penalty equal to Arata's Personal Honor. Gain 1 Honor."
Matsu_Arata = Personality(card_id=4892, title='Matsu Arata', force=3, chi=3, personal_honor=4, gold_cost=7, honor_requirement=7, clan=[LionClan], keywords=[Justicar, Paragon, Samurai, SoulOf('Matsu Nishijo')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Hachiro has +2F while attacking.'
Matsu_Hachiro = Personality(card_id=4915, title='Matsu Hachiro', force=1, chi=3, personal_honor=3, gold_cost=4, honor_requirement=6, clan=[LionClan], keywords=[Samurai, SoulOf('Matsu Gohei')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Fear Battle:</b> Target an enemy unit: Bow each card in it with equal or lower Force than Hana. Gain 1 Honor for each card this bowed.'
Matsu_Hana = Personality(card_id=4916, title='Matsu Hana', force=5, chi=3, personal_honor=4, gold_cost=9, honor_requirement=6, clan=[LionClan], keywords=[Unique, Paragon, Samurai, SoulOf('Matsu Fumiyo Experienced')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'Ranged Attacks may not target cards in this unit.'
Matsu_Yuuto = Personality(card_id=5010, title='Matsu Yuuto', force=4, chi=4, personal_honor=2, gold_cost=8, honor_requirement=5, clan=[LionClan], keywords=[Cavalry, Samurai, SoulOf('Matsu Agetoki')], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])