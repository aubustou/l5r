from __future__ import annotations
from ..common import Personality
from l5r_auto.clans import ShadowlandsFaction, Unaligned
from l5r_auto.keywords import Commander, Conqueror, Earth, Gaijin, Golem, Jackal, Mercenary, Nonhuman, Shadowlands, Shugenja, Unique, Wani, Yodotai
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition
'After Abdollah enters play, lose 2 Honor and create a 2F/2C/0PH <b>Nonhuman &#149; Shadowlands &#149; Undead</b> Personality.'
Abdollah = Personality(card_id=10667, title='Abdollah', force=1, chi=2, personal_honor=0, gold_cost=6, honor_requirement=None, clan=[Unaligned], keywords=[Gaijin, Jackal, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"After Boyoh Mercenary enters play, discard a card.<br>After Boyoh Mercenary's army destroys a Province, draw a card."
Boyoh_Mercenary = Personality(card_id=10669, title='Boyoh Mercenary', force=3, chi=2, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[Unaligned], keywords=[Mercenary], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Hikano enters play, lose 1 Honor.<br><b>Home Battle, :bow::</b> Straighten your target Oni. <i>(Home actions may be taken from home.)</i><br><b>Maho Limited:</b> Destroy a target Ikoma Ayumu. Destroy Hikano.'
Chuda_Hikano = Personality(card_id=10665, title='Chuda Hikano', force=2, chi=3, personal_honor=0, gold_cost=5, honor_requirement=None, clan=[Unaligned, ShadowlandsFaction], keywords=[Shadowlands, Shugenja], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Battle/Open:</b> Destroy your target Personality. Give Hoshoku-sha +2F.'
Hoshokusha = Personality(card_id=10670, title='Hoshoku-sha', force=4, chi=1, personal_honor=0, gold_cost=7, honor_requirement=None, clan=[Unaligned], keywords=[Nonhuman, Wani], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After Legulus enters play, lose 2 Honor.<br>Melee and Ranged Attacks targeting cards in this unit have -3 strength.<br><b>Limited:</b> Search your deck for a Yodotai Legionnaire Follower. Show it. Put it in your hand.'
Legulus = Personality(card_id=10668, title='Legulus', force=4, chi=4, personal_honor=0, gold_cost=10, honor_requirement=None, clan=[Unaligned], keywords=[Conqueror, Unique, Commander, Gaijin, Yodotai], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'After The Lost Colossus enters play, bow it.<br>Will not attach cards. Will not challenge. You may not target The Lost Colossus with Political actions.'
The_Lost_Colossus = Personality(card_id=10666, title='The Lost Colossus', force=6, chi=5, personal_honor=0, gold_cost=8, honor_requirement=None, clan=[Unaligned], keywords=[Earth, Golem, Nonhuman], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])