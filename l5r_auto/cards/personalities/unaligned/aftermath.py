from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import BrotherhoodOfShinsei, ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Courtier, Earth, Experienced, Fudo, Gaijin, Heir, Imperial, Kitsune, Monk, Nonhuman, OnyxChampion, Paragon, Samurai, Shadowlands, Shugenja, Unique, Yodotai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After Isidoros enters play, lose 2 Honor.<br><b>Battle:</b> Straighten your target Follower.'
Isidoros = Personality(card_id=10880, title='Isidoros', force=3, chi=2, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Gaijin, Yodotai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Seiken will not be dishonored or gain a Clan Alignment.<br><b>Interrupt:</b> After you Recruit Seiken, Recruit a non-Unique Samurai with lower Gold Cost, ignoring costs.<br><b>Political Open, :bow::</b> Take the Imperial Favor.'
Iweko_Seiken = Personality(card_id=10881, title='Iweko Seiken', force=3, chi=4, personal_honor=4, gold_cost=11, honor_requirement=7, clan=[Unaligned], keywords=[Unique, Heir, Imperial, Paragon, Samurai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"Spider Clan players ignore Shibatsu's Honor Requirement. Will not gain a Clan Alignment.<br>After Shibatsu enters play, gain 3 Honor.<br>After Shibatsu leaves play, lose 10 Honor.<br><b>Limited, :bow::</b> Gain 1 Honor."
Iweko_Shibatsu = Personality(card_id=10882, title='Iweko Shibatsu', force=1, chi=3, personal_honor=4, gold_cost=6, honor_requirement=10, clan=[Unaligned], keywords=[Unique, Courtier, Heir, Imperial], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Kichi enters play, lose 3 Honor and create a 4F/2C/0PH <b>Badger &#149; Nonhuman &#149; Shadowlands &#149; Spirit</b> Personality with the ability, "<b>Battle, :bow::</b> Melee 4 Attack."'
Kitsune_Kichi_Experienced = Personality(card_id=10883, title='Kitsune Kichi', force=0, chi=4, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Unique, Earth, Experienced('1'), Kitsune, Nonhuman, OnyxChampion, Shadowlands, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Usui enters play, lose 1 Honor.<br><b>Earth Battle:</b> Give this Province +2 strength.'
Usui = Personality(card_id=10884, title='Usui', force=3, chi=4, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[Unaligned, BrotherhoodOfShinsei], keywords=[Earth, Fudo, Monk], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])