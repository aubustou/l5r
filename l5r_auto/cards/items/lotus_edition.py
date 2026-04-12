from __future__ import annotations
from .common import Item
from l5r_auto.keywords import Shadowlands
from l5r_auto.legality import DiamondEdition, GoldEdition, IvoryEdition, LotusEdition, ModernEdition, TwentyFestivalsEdition
'After you Equip this Item, lose 4 Honor.<br>This Personality has <b>Cavalry</b>. <br><b>Battle:</b> Fear 2.'
Hellbeast = Item(card_id=3053, title='Hellbeast', force=2, chi=0, gold_cost=4, focus_value=2, keywords=[Shadowlands], traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, LotusEdition, GoldEdition, DiamondEdition, ModernEdition])