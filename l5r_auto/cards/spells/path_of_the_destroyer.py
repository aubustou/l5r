from __future__ import annotations
from .common import Spell
from l5r_auto.keywords import Air
from l5r_auto.legality import CelestialEdition, IvoryEdition, ModernEdition, OnyxEdition, TwentyFestivalsEdition
'Attaches to an Earth Shugenja for 2 less Gold.<br><b>Earth Battle, :bow::</b> Give each of your Shugenja in this army +1F.'
Earths_Embrace = Spell(card_id=2261, title="Earth's Embrace", gold_cost=2, focus_value=1, traits=[], abilities=[], legality=[TwentyFestivalsEdition, CelestialEdition, OnyxEdition, ModernEdition])
'<b>Air Open:</b> Transfer this Spell to your target Air Shugenja. <br><b>Air Battle, :bow::</b> If this Shugenja is opposed, give this Province +2 strength and gain 1 Honor. Move this Shugenja home.'
Shielded_by_Tempest = Spell(card_id=6842, title='Shielded by Tempest', gold_cost=2, focus_value=4, keywords=[Air], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, CelestialEdition, ModernEdition])