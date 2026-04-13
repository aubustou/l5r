from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import IvoryEdition, JadeEdition, ModernEdition, TwentyFestivalsEdition
'<b>Interrupt:</b> After any Fear effect from the action bows a card, destroy it.'
Okura_is_Released = Strategy(card_id=5688, title='Okura is Released', focus_value=3, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, JadeEdition, ModernEdition])