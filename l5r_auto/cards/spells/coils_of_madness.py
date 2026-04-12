from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air, Earth, Fire, Koan, Thunder, Unique, Void, Weapon
from l5r_auto.legality import EmperorEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
"<b>Air Open:</b> If this Shugenja is unbowed, target a Personality with Force equal to or less than this Shugenja's Chi. Give the target and each of his Followers Cavalry. Bow this Shugenja."
Among_the_Clouds = Spell(card_id=10542, title='Among the Clouds', gold_cost=0, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'Attaches to a Thunder Shugenja for 1 less Gold.<br><b>Thunder Battle, :bow::</b> Give this Shugenja +2F.'
Blade_of_Storms = Spell(card_id=10541, title='Blade of Storms', gold_cost=1, focus_value=3, keywords=[Weapon, Thunder], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Fire Open, :bow::</b> Destroy a target attachment.'
Flame_Lash = Spell(card_id=10539, title='Flame Lash', gold_cost=3, focus_value=1, keywords=[Fire], traits=[], abilities=[], legality=[EmperorEdition, ModernEdition])
'<b>Limited:</b> If this Shugenja is unbowed, put a Spell in your discard pile into your hand. Bow this Shugenja. Remove this Spell from the game.'
Hidden_Power = Spell(card_id=10536, title='Hidden Power', gold_cost=2, focus_value=1, keywords=[Unique], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Void Limited, :bow::</b> Reduce a Province's strength to 0. If its player has two or more Provinces, you may remove five Koan cards you control from the game to destroy it."
Koans_Whisper = Spell(card_id=10540, title="Koan's Whisper", gold_cost=5, focus_value=4, keywords=[Unique, Koan, Void], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Earth Battle, :bow::</b> Give your target defending Personality a Force bonus equal to his Personal Honor plus 1.'
Soul_of_Earth = Spell(card_id=10538, title='Soul of Earth', gold_cost=0, focus_value=2, keywords=[Earth], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
"<b>Air Open:</b> If this Shugenja is unbowed, give a target Personality or Follower a Force penalty equal to this Shugenja's Chi. Bow this Shugenja."
Tempest_of_Air = Spell(card_id=10537, title='Tempest of Air', gold_cost=2, focus_value=3, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, EmperorEdition, ModernEdition])
'<b>Water Battle:</b> Move a target Personality at any location to the current battlefield. Straighten his unit if you do not control him. Destroy this Spell.'
Typhoon_Surge = Spell(card_id=10543, title='Typhoon Surge', gold_cost=2, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, EmperorEdition, OnyxEdition, ModernEdition])