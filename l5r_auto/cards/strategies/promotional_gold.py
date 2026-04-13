from __future__ import annotations
from .common import Strategy
from l5r_auto.legality import GoldEdition, IvoryEdition, ModernEdition, TwentyFestivalsEdition
'<b>Interrupt:</b> After your Personality wins any duel created by the action, permanently give him the ability, "<b>Battle:</b> Fear 4." You cannot gain Honor from the action.'
Feared_Duelist = Strategy(card_id=2495, title='Feared Duelist', gold_cost=0, focus_value=2, traits=[], abilities=[], legality=[IvoryEdition, TwentyFestivalsEdition, GoldEdition, ModernEdition])