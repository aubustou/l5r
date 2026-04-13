from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Earth, Fire, Void, Water
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'<b>Open, :bow::</b> Give your target Spirit <b>Expendable</b> <i>(Draw a card after your Expendable card is destroyed)</i>.'
Banished_from_the_Realm = Spell(card_id=10913, title='Banished from the Realm', gold_cost=1, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Water Battle, :bow::</b> Give a target Personality or Follower a Force penalty equal to your target Personality's Chi."
Blistering_Rain = Spell(card_id=10914, title='Blistering Rain', gold_cost=1, focus_value=1, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Shugenja has <b>Cavalry</b> while he is Shadowlands.<br><b>Open, :bow::</b> Give a target Nonhuman card <b>Cavalry</b>.'
Chikushudos_Infusion = Spell(card_id=10915, title="Chikushudo's Infusion", gold_cost=2, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'This Shugenja has the element keywords of every Ring you control.<br><b>Open, :bow::</b> Bow your target unbowed Ring. Straighten this Shugenja.'
Drawing_on_All_Things = Spell(card_id=10916, title='Drawing on All Things', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Battle resolution will not destroy cards in this unit while defending and, if this Shugenja is Earth, while attacking.'
Hitomis_Devotion = Spell(card_id=10917, title="Hitomi's Devotion", gold_cost=2, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
'<b>Void Battle, :bow::</b> Give a target Personality +1F, or +2F if this Shugenja or the Personality is Void or a Yojimbo.'
Mystical_Augmentation = Spell(card_id=10918, title='Mystical Augmentation', gold_cost=1, focus_value=3, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, ModernEdition])
'<b>Void Interrupt, :bow::</b> Give the first card discarded by the action +1FV or -1FV. <i>(This does not affect cards focused in a duel)</i>.'
Reverse_Fate = Spell(card_id=10919, title='Reverse Fate', gold_cost=0, focus_value=4, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Thunder Battle, :bow::</b> Target your Personality. Ranged Attack with strength equal to his Chi. Destroy this Spell.'
Sailors_Warning = Spell(card_id=10920, title="Sailor's Warning", gold_cost=0, focus_value=1, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])
"<b>Repeatable Fire Battle:</b> Discard a card to make a Ranged Attack with strength equal to its Focus Value or this Shugenja's Chi, whichever is higher. <i>(Repeatable actions may be used any number of times per turn.)</i>"
Searing_Siege = Spell(card_id=10921, title='Searing Siege', gold_cost=3, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"While this Shugenja is defending, other players' cards will not bow him."
The_Earths_Armor = Spell(card_id=10922, title="The Earth's Armor", gold_cost=1, focus_value=2, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Air Open, :bow::</b> Bow this Shugenja to create a 2C/0PH <b>Illusion &#149; Samurai &#149; Spirit</b> Personality with Force equal to this Shugenja's Chi, plus 1 if he is Air. Destroy this Spell."
The_Winds_Champion = Spell(card_id=10923, title="The Wind's Champion", gold_cost=7, focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Earth Limited, :bow::</b> Create a 1F <b>Clay Soldier &#149; Nonhuman &#149; Yojimbo</b> Follower and attach it to your target Shugenja without Followers.'
Yojimbo_of_Earth = Spell(card_id=10924, title='Yojimbo of Earth', gold_cost=2, focus_value=3, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])