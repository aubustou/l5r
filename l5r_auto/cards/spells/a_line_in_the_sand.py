from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Jade, Kharmic, Thunder, Void, Water
from l5r_auto.legality import IvoryEdition, ModernEdition, TwentyFestivalsEdition
'Attaches to a Fire Shugenja for 1 less Gold.<br><b>Fire Battle/Engage, :bow::</b> Target this Shugenja or your Samurai. Give him +2F/+2C; he may not issue challenges this turn.'
Burning_Spirit = Spell(card_id=11651, title='Burning Spirit', gold_cost=2, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'This Spell\'s Invest effects last while it remains attached to the Shugenja.<br><b>Invest :g1::</b> This Shugenja has <b>Cavalry</b>.<br><b>Invest :g2::</b> This Shugenja has <b>Conqueror</b>.<br><b>Invest :g3::</b> This Shugenja has +2F.<br><b>Invest :g4::</b> This Shugenja has the ability, "<b>Battle:</b> Ranged 3 Attack."'
Guidance_in_War = Spell(card_id=11652, title='Guidance in War', gold_cost=0, focus_value=4, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'Equips to a Water Shugenja for 1 less Gold.<br><b>Water Battle, :bow::</b> Move a target defending Personality home.'
Impassable_Waters = Spell(card_id=11653, title='Impassable Waters', gold_cost=1, focus_value=2, keywords=[Water], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"While this Shugenja is Fire, he has <b>Resilient</b>. <i>(Once per game per card, a Resilient card does not die in battle resolution.)</i><br><b>Fire Battle:</b> Fear equal to your target Personality's Chi. Destroy this Spell."
Light_of_the_Morning_Sun = Spell(card_id=11654, title='Light of the Morning Sun', gold_cost=0, focus_value=2, keywords=[Fire], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After you Equip this Spell to a Void Shugenja, draw a card.<br><b>Void Open, :bow::</b> Bow or straighten a target Sensei.'
Past_and_Future = Spell(card_id=11655, title='Past and Future', gold_cost=0, focus_value=4, keywords=[Kharmic, Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Invest :g1::</b> Draw a card.<br><b>Void Open, :bow::</b> Turn a target card in a Province face-up, or one to two such cards if this Shugenja is Void. Give -3 strength to each Province in which the target is an Unaligned Personality.'
See_the_Souls_Past = Spell(card_id=11656, title="See the Soul's Past", gold_cost=0, focus_value=1, keywords=[Void], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'After you Equip this Spell, give this Shugenja a number of +1F Rock tokens equal to his Chi.<br><b>Earth Jade Repeatable Battle, :bow::</b> Fear 3. You may discard two Rock tokens from this Shugenja, or one if he is Earth, to straighten this Spell.'
Stones_of_Purity = Spell(card_id=11657, title='Stones of Purity', gold_cost=5, focus_value=3, keywords=[Earth, Jade], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
"This Shugenja may not Equip another copy of Suspending Wind unless he is Air.<br><b>Air Open, :bow::</b> Target a face-up Personality in a Province. Increase his Gold Cost by half this Shugenja's Chi, rounded up."
Suspending_Wind = Spell(card_id=11658, title='Suspending Wind', gold_cost=1, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])
'<b>Fire Thunder Battle, :bow::</b> Bow a target attachment, or a target Personality without attachments and with equal or lower Chi than this Shugenja. Destroy the target if it is a Weapon and this Shugenja is Fire or Thunder.'
Thundering_Waves = Spell(card_id=11659, title='Thundering Waves', gold_cost=0, focus_value=2, keywords=[Fire, Thunder], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, ModernEdition])